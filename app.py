from flask import Flask, request, jsonify, render_template
import joblib
import emoji
import re

app = Flask(__name__)

def custom_tokenizer(text):
    # This regex pattern will match words and emojis
    pattern = r'\w+|[^\w\s]'
    return re.findall(pattern, text)

# Load the saved model and vectorizer
model = joblib.load('naive_bayes_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get the input from the form
    user_input = request.form['user_input']

    # Convert emojis to text
    user_input = emoji.demojize(user_input)
    
    # Transform the input data using the loaded vectorizer
    transformed_input = vectorizer.transform([user_input])
    
    # Make a prediction
    prediction = model.predict(transformed_input)[0]
    
    # Map the prediction to a sentiment label
    sentiment_map = {0: "Negative", 1: "Neutral", 2: "Positive"}
    sentiment = sentiment_map[prediction]
    
    # Return the result
    return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

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
    
    # Transform the input data using the loaded vectorizer
    transformed_input = vectorizer.transform([user_input])
    
    # Make a prediction
    prediction = model.predict(transformed_input)[0]
    
    # Map the prediction to a sentiment label
    sentiment_map = {0: "negative", 1: "neutral", 2: "positive"}
    sentiment = sentiment_map[prediction]
    
    # Return the result
    return render_template('index.html', prediction=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

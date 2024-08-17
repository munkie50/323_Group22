# CSCI322 Group Project

## Installation Instructions

### Step 1: Install Git  
Head to **(https://git-scm.com/download/win)** and download instllation file.  
Go through Installer with default options.    

### Step 2: Install Git Pull Requests and Issues VSCode Extension  
Head to extensions tab on VSCode.  
Search and install 'Git Pull Requests' Extension  

### Step 3: Clone Repo  
Run **git clone https://github.com/munkie50/323_Group22.git** command in the directory of your choice.  
Log into Github when prompted.  

## Editting on main

### Fetch changes from main before editing  
git fetch origin  
git pull origin main  

### Commiting and Pushing Changes  
git add .  
git commit -m "Message"  
git push origin main  

## Editting on a branch

### Fetch changes from main before editing  
git fetch origin  
git pull origin main  

### Create new branch for your feature or switch to existing branch  
#### For new branch  
git checkout -b branch-name  
#### For existing branch
git checkout branch-name  

### Commiting and Pushing Changes  
git add .  
git commit -m "Message"  
git push origin branch-name  

### Creating a Pull Request  
Go to Github page of your branch.  
Click "Compare & Pull Request".  
Enter description of changes made and submit pull request.  

## Useful Git Commands:
git status (To check current status of your git progress)  
  
git fetch (To fetch Teammates changes before starting) 
  
git pull (To confirm pull in Teammates changes)  
  
git checkout -b <new-branch-name> (Creates a new branch for a new feature)  
  
git checkout <branch-name> (Switch to another branch)  
  
git push origin <new-branch-name> (Push new branch from local machine to main)  
  
git commit -m (To commit changes to current branch, and include a message)  

git push (To push changes to the main repo)

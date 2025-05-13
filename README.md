# Paudit
Paudit is a password strength auditor that evaluates passwords against common vulnerabilities and security best practices. It provides a detailed analysis of password strength by checking for common weaknesses, estimating entropy, and calculating realistic breakthrough times for attackers.

## Features
- **Common Password Checking**: Checks against 10,000+ common passwords
- **Entropy**: Calculates bit entropy
- **Breakthrough**: Estimates realistic breakthrough time with modern GPU cracking
- **Feedback & Suggestions**: Provides improvement suggestions
- **CLI**: Works as both CLI tool and importable Python module
  
## How it works
- The user inputs a password
- The program compares the password to the `password.txt` file
- If the password is too common and is in the list of `password.txt` then the program prompts the user to try again, otherwise the program gives the user feedback
- The program asks the user to try another password, with `y` indicating yes and `n` indicating no, choosing yes allows you to try again, and choosing no ends the program
   
## Installation
1. Download the lastest version of Python on your device
2. Download the files from the Paudit folder: `Paudit.py` & `passwords.txt`
3. Save both files in the same folder

## Usage
1. Open the IDE of your choice (VScode, Notepad, etc)
2. Open the folder with the files 
3. Open the terminal and type `python paudit.py`
4. Run the program 
5. Type in your password and have fun

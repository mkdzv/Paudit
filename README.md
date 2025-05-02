# Paudit
Paudit is a password strength auditor that evaluates passwords against common vulnerabilities and security best practices. It provides a detailed analysis of password strength by checking for common weaknesses, estimating entropy, and calculating realistic breakthrough times for attackers.

## Features
- **Common Password Checking**: Checks against 10,000+ common passwords
- **Entropy**: Calculates bit entropy
- **Breakthrough**: Estimates realistic breakthrough time with modern GPU cracking
- **Feedback & Suggestions**: Provides improvement suggestions
- **CLI**: Works as both CLI tool and importable Python module
  
## How it works
1. The user inputs a password
2. The program compares the password to the `password.txt` file
3. If the password is too common and is in the list of `password.txt` then the program prompts the user to try again, otherwise the program gives the user feedback, entropy, breakthrough time and suggestions for improvement
4. The program asks the user to try another password, with `y` indicating yes and `n` indicating no, choosing yes allows you to try another password, and choosing no ends the program
5. Enjoy :)
   
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
  
## License
MIT License

Copyright (c) 2025 mkdzv

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

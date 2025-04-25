# Paudit
Paudit is a password strength auditor that evaluates passwords against common vulnerabilities and security best practices. It provides a detailed analysis of password strength by checking for common weaknesses, estimating entropy, and calculating realistic breakthrough times for attackers.

## Features
- Checks against 10,000+ common passwords
- Calculates bit entropy for cryptographic strength
- Estimates realistic breakthrough time with modern GPU cracking
- Provides improvement suggestions
- Works as both CLI tool and importable Python module
  
## How it works

## Installation

## Usage

## Example

    ██████╗  █████╗ ██╗   ██╗██████╗ ██╗████████╗
    ██╔══██╗██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
    ██████╔╝███████║██║   ██║██║  ██║██║   ██║   
    ██╔═══╝ ██╔══██║██║   ██║██║  ██║██║   ██║   
    ██║     ██║  ██║╚██████╔╝██████╔╝██║   ██║   
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝
    Simple Password Auditor

Enter password to audit: hearmeout123#@!

🔒 Password Audit Results:
------------------------------------------------------------
Password: hearmeout123#@!
Length: 15 characters
- ✅ Good length (15 characters)
- ❌ Add uppercase letters
- ✅ Contains lowercase letters
- ✅ Contains numbers
- ✅ Contains special characters
- ✅ Good mix of character types
- ❌ Avoid sequential numbers (e.g., 123, 456)
- 🔐 Entropy: 90.67 bits
- ⏳ Estimated breakthrough time: 6228054813 years, 10 months

⚠️ Good password - could be stronger
------------------------------------------------------------
Security Score: 75/100

Audit another password? (y/n):

## Contribute

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

## Demo

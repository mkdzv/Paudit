# Paudit
Paudit is a Python-based password strength auditor that evaluates passwords against common vulnerabilities and security best practices. It provides a detailed analysis of password strength by checking for common weaknesses, estimating entropy, and calculating realistic breakthrough times for attackers.

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

## Demo

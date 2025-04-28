#!/usr/bin/env python3
"""
Test script for Paudit - Password Auditor Tool

This script provides an easy way to test the password auditor with:
1. Pre-defined test cases
2. Interactive mode
3. File-based testing
"""

import sys
import os
from paudit import PasswordAuditor

def run_predefined_tests():
    """Run a series of predefined test cases"""
    print("\n" + "="*60)
    print("Running predefined test cases...")
    print("="*60)
    
    auditor = PasswordAuditor()
    
    test_cases = [
        ("123456", "Common password should fail"),
        ("password", "Common password should fail"),
        ("P@ssw0rd!", "Strong password should pass"),
        ("abc", "Too short should fail"),
        ("qwertyuiop", "Common keyboard pattern should fail"),
        ("JohnDoe1975", "Moderate password"),
        ("7s&4L*9p#2z", "Very strong password"),
        ("111111", "Repeated digits should fail"),
        ("Admin123", "Moderate but common pattern"),
        ("Tr0ub4dor&3", "Example from xkcd comic")
    ]
    
    for password, description in test_cases:
        print(f"\nTest Case: {description}")
        print("-" * 50)
        auditor.audit_password(password)

def interactive_test():
    """Run interactive testing mode"""
    print("\n" + "="*60)
    print("Interactive testing mode")
    print("="*60)
    
    auditor = PasswordAuditor()
    
    while True:
        password = input("\nEnter a password to test (or 'q' to quit): ")
        if password.lower() == 'q':
            break
        auditor.audit_password(password)

def test_from_file(filename):
    """Test passwords from a file (one per line)"""
    print(f"\nTesting passwords from file: {filename}")
    
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found", file=sys.stderr)
        return
    
    auditor = PasswordAuditor()
    
    with open(filename, 'r') as f:
        for line in f:
            password = line.strip()
            if password:  # Skip empty lines
                print(f"\nTesting: {password}")
                auditor.audit_password(password)

def main():
    print("""
    ████████╗███████╗███████╗████████╗
    ╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝
       ██║   █████╗  ███████╗   ██║   
       ██║   ██╔══╝  ╚════██║   ██║   
       ██║   ███████╗███████║   ██║   
       ╚═╝   ╚══════╝╚══════╝   ╚═╝   
    Paudit Test Script                 
    """)
    
    print("Choose testing mode:")
    print("1. Run predefined test cases")
    print("2. Interactive mode")
    print("3. Test passwords from file")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        run_predefined_tests()
    elif choice == "2":
        interactive_test()
    elif choice == "3":
        filename = input("Enter filename with passwords to test: ")
        test_from_file(filename)
    elif choice == "4":
        print("Exiting...")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Paudit - Password Auditor Tool
Checks password strength against common weak passwords and basic rules
"""

import sys
import math
from getpass import getpass

class PasswordAuditor:
    def __init__(self):
        self.common_passwords = self.load_common_passwords()
        self.min_length = 8
        self.special_chars = "!@#$%^&*()-_=+[{]}\\|;:'\",<.>/?"
        
        # For realistic breakthrough time estimation
        self.guesses_per_second = 1e10  # Modern GPU cluster can make ~10 billion guesses/sec

    def load_common_passwords(self):
        """Load common passwords from passwords.txt file"""
        try:
            with open('passwords.txt', 'r', encoding='utf-8') as f:
                return {line.strip() for line in f}
        except FileNotFoundError:
            print("Warning: passwords.txt not found. Using built-in common passwords.", file=sys.stderr)
            return {
                '123456', 'password', '12345678', 'qwerty', '123456789',
                '12345', '1234', '111111', '1234567', 'dragon',
                '123123', 'baseball', 'abc123', 'football', 'monkey',
                'letmein', 'shadow', 'master', '666666', 'qwertyuiop'
            }

    def calculate_entropy(self, password):
        """Calculate password entropy in bits"""
        if not password:
            return 0
            
        # Determine the character pool size
        pool_size = 0
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.special_chars for c in password)
        
        if has_lower:
            pool_size += 26
        if has_upper:
            pool_size += 26
        if has_digit:
            pool_size += 10
        if has_special:
            pool_size += len(self.special_chars)
            
        # If no character types detected, assume lowercase letters
        if pool_size == 0:
            pool_size = 26
            
        # Calculate entropy
        entropy = len(password) * math.log2(pool_size)
        return entropy

    def estimate_breakthrough_time(self, entropy):
        """
        Estimate realistic breakthrough time based on entropy
        Returns human-readable string
        """
        if entropy < 1:
            return "instantly"
            
        # Total possible guesses = 2^entropy
        total_guesses = 2 ** entropy
        seconds = total_guesses / self.guesses_per_second
        
        # Convert seconds to human-readable format
        if seconds < 1:
            return "instantly"
        
        intervals = (
            ('years', 31536000),
            ('months', 2592000),
            ('weeks', 604800),
            ('days', 86400),
            ('hours', 3600),
            ('minutes', 60),
            ('seconds', 1)
        )
        
        result = []
        for name, count in intervals:
            value = seconds // count
            if value:
                seconds -= value * count
                if value == 1:
                    name = name.rstrip('s')
                result.append(f"{int(value)} {name}")
        
        # Return the two most significant units
        return ', '.join(result[:2])

    def check_strength(self, password):
        """Check password strength and return feedback"""
        feedback = []
        score = 0  # Starting score (out of 100)

        # Check against common passwords (immediate failure if found)
        if password.lower() in self.common_passwords:
            feedback.append("❌ Password is too common - do not use it, try another password")
            return 0, feedback

        # Length check (max 25 points)
        length_points = min(len(password) * 2, 25)  # 2 points per character up to 25
        score += length_points
        if len(password) < self.min_length:
            feedback.append(f"❌ Too short (minimum {self.min_length} characters)")
        else:
            feedback.append(f"✅ Good length ({len(password)} characters)")

        # Complexity checks (75 points total)
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.special_chars for c in password)
        complexity_count = sum([has_upper, has_lower, has_digit, has_special])

        # Add points for each complexity type
        if has_upper:
            score += 15
            feedback.append("✅ Contains uppercase letters")
        else:
            feedback.append("❌ Add uppercase letters")

        if has_lower:
            score += 15
            feedback.append("✅ Contains lowercase letters")
        else:
            feedback.append("❌ Add lowercase letters")

        if has_digit:
            score += 15
            feedback.append("✅ Contains numbers")
        else:
            feedback.append("❌ Add numbers")

        if has_special:
            score += 15
            feedback.append("✅ Contains special characters")
        else:
            feedback.append("❌ Add special characters")

        # Bonus points for multiple complexity types
        if complexity_count >= 3:
            score += 15
            feedback.append("✅ Good mix of character types")
        elif complexity_count == 2:
            score += 5
            feedback.append("⚠️ Could use more character variety")

        # Sequential characters check (negative points)
        if any(password[i:i+3].isdigit() and 
               int(password[i]) + 1 == int(password[i+1]) and 
               int(password[i+1]) + 1 == int(password[i+2]) 
               for i in range(len(password)-2)):
            score -= 10
            feedback.append("❌ Avoid sequential numbers (e.g., 123, 456)")

        # Repeated characters check
        if any(c * 3 in password for c in password):
            score -= 10
            feedback.append("❌ Avoid repeated characters (e.g., aaa, 111)")

        # Calculate entropy
        entropy = self.calculate_entropy(password)
        feedback.append(f"🔐 Entropy: {entropy:.2f} bits")
        
        # Estimate breakthrough time
        breakthrough_time = self.estimate_breakthrough_time(entropy)
        feedback.append(f"⏳ Estimated breakthrough time: {breakthrough_time}")

        # Feedback based on score
        if score >= 80:
            feedback.append("\n✅ Excellent password!")
        elif score >= 60:
            feedback.append("\n⚠️ Good password - could be stronger")
        elif score >= 40:
            feedback.append("\n⚠️ Moderate password - needs improvement")
        else:
            feedback.append("\n❌ Weak password - not recommended")

        return score, feedback

    def audit_password(self, password=None):
        """Main auditing function"""
        if password is None:
            password = input("Enter password to audit: ")  # Changed from getpass to input
        
        print("\n🔒 Password Audit Results:")
        print("-" * 60)
        
        # Show the actual password instead of masking it
        print(f"Password: {password}")
        
        score, feedback = self.check_strength(password)
        print(f"Length: {len(password)} characters")
        
        for item in feedback:
            print(item)
        
        print("-" * 60)
        print(f"Security Score: {score}/100\n")
        return score

def main():
    print("""
    ██████╗  █████╗ ██╗   ██╗██████╗ ██╗████████╗
    ██╔══██╗██╔══██╗██║   ██║██╔══██╗██║╚══██╔══╝
    ██████╔╝███████║██║   ██║██║  ██║██║   ██║   
    ██╔═══╝ ██╔══██║██║   ██║██║  ██║██║   ██║   
    ██║     ██║  ██║╚██████╔╝██████╔╝██║   ██║   
    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚═╝   ╚═╝   
    Simple Password Auditor                         
    """)

    auditor = PasswordAuditor()
    
    if len(sys.argv) > 1:
        # Audit password from command line argument
        auditor.audit_password(sys.argv[1])
    else:
        # Interactive mode
        while True:
            auditor.audit_password()
            if input("Audit another password? (y/n): ").lower() != 'y':
                break

if __name__ == "__main__":
    main()
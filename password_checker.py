import re
from typing import Tuple, List

print("Password Strength Checker")


def check_password_strength(password: str) -> Tuple[str, int, List[str]]:
    """
    Check the strength of a password and return feedback.
    
    Args:
        password: The password to check
        
    Returns:
        Tuple containing:
        - strength_level: "Very Weak", "Weak", "Fair", "Good", or "Strong"
        - score: Strength score (0-100)
        - feedback: List of suggestions for improvement
    """
    score = 0
    feedback = []
    
    # Length checks
    if len(password) >= 8:
        score += 10
    else:
        feedback.append("Password should be at least 8 characters long")
    
    if len(password) >= 12:
        score += 10
    else:
        feedback.append("Consider using 12 or more characters for better security")
    
    if len(password) >= 16:
        score += 10
    
    # Character type checks
    if re.search(r'[a-z]', password):
        score += 15
    else:
        feedback.append("Add lowercase letters (a-z)")
    
    if re.search(r'[A-Z]', password):
        score += 15
    else:
        feedback.append("Add uppercase letters (A-Z)")
    
    if re.search(r'\d', password):
        score += 15
    else:
        feedback.append("Add numbers (0-9)")
    
    if re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password):
        score += 20
    else:
        feedback.append("Add special characters (!@#$%^&*...)")
    
    # Bonus for no common patterns
    common_patterns = ['123', '456', 'abc', 'password', 'qwerty', 'admin', 'letmein']
    if not any(pattern in password.lower() for pattern in common_patterns):
        score += 5
    else:
        feedback.append("Avoid common patterns like '123' or 'password'")
    
    # Determine strength level
    if score >= 90:
        strength_level = "Strong"
    elif score >= 70:
        strength_level = "Good"
    elif score >= 50:
        strength_level = "Fair"
    elif score >= 25:
        strength_level = "Weak"
    else:
        strength_level = "Very Weak"
    
    return strength_level, score, feedback


def display_password_analysis(password: str) -> None:
    """Display a detailed analysis of password strength."""
    strength_level, score, feedback = check_password_strength(password)
    
    print(f"\n{'='*50}")
    print(f"Password Analysis")
    print(f"{'='*50}")
    print(f"Strength Level: {strength_level}")
    print(f"Score: {score}/100")
    print(f"{'='*50}")
    
    if feedback:
        print("Suggestions for improvement:")
        for suggestion in feedback:
            print(f"  • {suggestion}")
    else:
        print("✓ Excellent! Your password is very strong.")
    
    print(f"{'='*50}\n")


def main():
    """Main function to run the password strength checker."""
    print("\n" + "="*50)
    print("Password Strength Checker")
    print("="*50)
    
    while True:
        password = input("\nEnter a password to check (or 'quit' to exit): ").strip()
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
        
        if not password:
            print("Please enter a password.")
            continue
        
        display_password_analysis(password)


if __name__ == "__main__":
    main()

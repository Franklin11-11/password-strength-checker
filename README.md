# Password Strength Checker

A Python-based password strength checker that evaluates passwords against several security criteria and provides a score, strength level, and recommendations for improvement.

## Features

- Checks password length
- Detects lowercase letters
- Detects uppercase letters
- Detects numbers
- Detects special characters
- Checks for common password patterns
- Calculates a password strength score from 0–100
- Classifies passwords as:
  - Very Weak
  - Weak
  - Fair
  - Good
  - Strong
- Provides feedback to help improve password security

## Scoring System

The checker evaluates passwords using the following criteria:

| Criteria | Points |
|---|---:|
| At least 8 characters | +10 |
| At least 12 characters | +10 |
| At least 16 characters | +10 |
| Lowercase letter | +15 |
| Uppercase letter | +15 |
| Number | +15 |
| Special character | +20 |
| No common patterns | +5 |
| **Maximum** | **100** |

### Strength Levels

| Score | Strength |
|---:|---|
| 90–100 | Strong |
| 70–89 | Good |
| 50–69 | Fair |
| 25–49 | Weak |
| 0–24 | Very Weak |

## Technologies Used

- Python 3
- Regular Expressions (`re`)
- `unittest`
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
password-strength-checker/
│
├── password_checker.py
├── README.md
├── .gitignore
└── tests/
    └── test_password_checker.py
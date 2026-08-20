import unittest

from password_checker import check_password_strength


class TestPasswordStrengthChecker(unittest.TestCase):

    def test_very_weak_password(self):
        strength, score, feedback = check_password_strength("abc")

        self.assertEqual(strength, "Very Weak")
        self.assertLess(score, 25)
        self.assertTrue(len(feedback) > 0)

    def test_weak_password(self):
        strength, score, feedback = check_password_strength("password")

        self.assertEqual(strength, "Weak")
        self.assertGreaterEqual(score, 25)
        self.assertLess(score, 50)
        self.assertTrue(len(feedback) > 0)

    def test_fair_password(self):
        strength, score, feedback = check_password_strength("Password123")

        self.assertEqual(strength, "Fair")
        self.assertGreaterEqual(score, 50)
        self.assertLess(score, 70)

    def test_good_password(self):
        strength, score, feedback = check_password_strength("Password12345!")

        self.assertEqual(strength, "Good")
        self.assertGreaterEqual(score, 70)
        self.assertLess(score, 90)

    def test_strong_password(self):
        strength, score, feedback = check_password_strength("VeryStrongPassword123!")

        self.assertEqual(strength, "Strong")
        self.assertGreaterEqual(score, 90)
        self.assertEqual(score, 95)
        self.assertEqual(feedback, [])

    def test_missing_uppercase(self):
        strength, score, feedback = check_password_strength("verystrongpassword123!")

        self.assertIn("Add uppercase letters (A-Z)", feedback)

    def test_missing_number(self):
        strength, score, feedback = check_password_strength("VeryStrongPassword!")

        self.assertIn("Add numbers (0-9)", feedback)

    def test_missing_special_character(self):
        strength, score, feedback = check_password_strength("VeryStrongPassword123")

        self.assertIn(
            "Add special characters (!@#$%^&*...)",
            feedback
        )

    def test_common_pattern_warning(self):
        strength, score, feedback = check_password_strength("Password123!")

        self.assertIn(
            "Avoid common patterns like '123' or 'password'",
            feedback
        )


if __name__ == "__main__":
    unittest.main()
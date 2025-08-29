from unittest import TestCase
from password_checker import is_valid_password

class WhiteBoxTest(TestCase):

    def test_too_short(self):
        self.assertFalse(is_valid_password("A1b!"))

    def test_no_digit(self):
        self.assertFalse(is_valid_password("Password!"))

    def test_no_lowercase(self):
        self.assertFalse(is_valid_password("PASSWORD1!"))

    def test_no_uppercase(self):
        self.assertFalse(is_valid_password("password1!"))

    def test_all_conditions_met(self):
        self.assertTrue(is_valid_password("Password1+!"))

    def test_exact_boundary_length(self):
        self.assertTrue(is_valid_password("Abcd!f1G"))

    def test_no_special_chars(self):
        self.assertFalse(is_valid_password("Password1"))
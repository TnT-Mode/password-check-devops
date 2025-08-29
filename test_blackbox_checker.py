from unittest import TestCase
from password_checker import is_valid_password

class BlackBoxTest(TestCase):

    def test_valid_password(self):
        self.assertTrue(is_valid_password("Password109+?"))

    def test_short_password(self):
        self.assertFalse(is_valid_password("Sh0rt!"))

    def test_no_number_password(self):
        self.assertFalse(is_valid_password("testPassword!"))

    def test_no_capital_letters(self):
        self.assertFalse(is_valid_password("testpassw0rd!"))

    def test_no_small_letters(self):
        self.assertFalse(is_valid_password("PASSW0RD!"))

    def test_no_special_chars(self):
        self.assertFalse(is_valid_password("Password109"))

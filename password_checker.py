from re import compile

# password_checker.py
def is_valid_password(password: str):
    special_chars_reg = compile(r'(?=.*[^A-Za-z0-9])')

    """
    Gültiges Passwort erfüllt:
    - mind. 8 Zeichen
    - enthält Zahl
    - enthält Groß- und Kleinbuchstaben
    """
    if len(password) < 8:
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isupper() for c in password):
        return False
    if not special_chars_reg.match(password):
        return False
    return True

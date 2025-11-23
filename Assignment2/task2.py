import re

def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome when ignoring case, spaces and punctuation.
    """
    cleaned = re.sub(r'[^A-Za-z0-9]', '', s).lower()
    return cleaned == cleaned[::-1]

def user_input_palindrome():
    text = input("Enter text to check for palindrome: ")
    if is_palindrome(text):
        print("It's a palindrome.")
        return True
    else:
        print("Not a palindrome.")
        return False
    
def _name_():
    if _name_ == "_main_":
        user_input_palindrome()
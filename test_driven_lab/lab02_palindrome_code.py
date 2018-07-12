# See palindrome_test for instructions
def palindrome_check(string):
    if not isinstance(string, str):
        string = str(string)
    if (string.lower() == string.lower()[::-1]):
        return True
    else:
        return False

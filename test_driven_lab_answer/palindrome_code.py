# See palindrome_test for instructions


def palindrome_check(a_string):
    if not isinstance(a_string, str):
        a_string = str(a_string)
    if a_string.lower() == a_string.lower()[::-1]:
        return True
    else:
        return False

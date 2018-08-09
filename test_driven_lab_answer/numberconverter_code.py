# Instructions:
# Create a function that accepts a list of integers as an input and returns
# a list that contains each number spelled out. If the number is longer than
# a single digit, add the converted string of each digit together. For
# example the list [1,23,6,66,10] would be returned as
# [one,twothree,six,sixsix,onezero].
#
# You may use the following when creating the function:
#  - str() - converts a variable into a string


def numbers_to_names(number_list):
    out_list = []
    for number in number_list:
        digit_names = ''
        number_string = str(number)
        for digit in number_string:
            if digit == '1':
                digit_names = digit_names + 'one'
            elif digit == '2':
                digit_names = digit_names + 'two'
            elif digit == '3':
                digit_names = digit_names + 'three'
            elif digit == '4':
                digit_names = digit_names + 'four'
            elif digit == '5':
                digit_names = digit_names + 'five'
            elif digit == '6':
                digit_names = digit_names + 'six'
            elif digit == '7':
                digit_names = digit_names + 'seven'
            elif digit == '8':
                digit_names = digit_names + 'eight'
            elif digit == '9':
                digit_names = digit_names + 'nine'
            elif digit == '0':
                digit_names = digit_names + 'zero'
        out_list.append(digit_names)
    return out_list

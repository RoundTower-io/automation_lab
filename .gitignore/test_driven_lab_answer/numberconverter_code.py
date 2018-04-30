#Instructions:
#Create a function that accepts a list of integers as an input and returns 
#a list that contains each number spelled out. If the number is longer than
#a single digit, add the converted string of each digit together. For 
#example the list [1,23,6,66,10] would be returned as
#[one,twothree,six,sixsix,onezero]. If a value in the list is not an 
#integer, discard it.
#
#You may use the following when creating the function:
#* list() - converts a variable into a list
#* str() - converts a variable into a string

def convertlist(numberlist):
    return_list = []
    for number_convert in numberlist:
        if isinstance(number_convert, int):
            list_item = ''
            number_string = str(number_convert)
            for number_digit in list(number_string):
                if number_digit == '1':
                    list_item = list_item + 'one'
                elif number_digit == '2':
                    list_item = list_item + 'two'
                elif number_digit == '3':
                    list_item = list_item + 'three'
                elif number_digit == '4':
                    list_item = list_item + 'four'
                elif number_digit == '5':
                    list_item = list_item + 'five'
                elif number_digit == '6':
                    list_item = list_item + 'six'
                elif number_digit == '7':
                    list_item = list_item + 'seven'
                elif number_digit == '8':
                    list_item = list_item + 'eight'
                elif number_digit == '9':
                    list_item = list_item + 'nine'
                elif number_digit == '0':
                    list_item = list_item + 'zero'
            return_list.append(list_item)
    return return_list
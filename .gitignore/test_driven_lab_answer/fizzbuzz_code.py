#Instructions:
#Write a function that returns a number provided or returns a string based on the following: 
#*For each multiple of 3, return "Fizz" instead of the number. 
#*For each multiple of 5, return "Buzz" instead of the number. 
#*For numbers which are multiples of both 3 and 5, return "FizzBuzz" instead of the number.
def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 == 0):
        return 'FizzBuzz'
    elif (x % 3 == 0):
        return 'Fizz'
    elif (x % 5 == 0):
        return 'Buzz'
    else:
        return x
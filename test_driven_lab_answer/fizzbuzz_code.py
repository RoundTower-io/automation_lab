# Instructions:
# Write a function that returns a number provided or returns a
# string based on the following:
# - For each multiple of 3, return "Fizz"
# - For each multiple of 5, return "Buzz"
# - For numbers which are multiples of both 3 *and* 5, return "FizzBuzz"
# - Otherwise, just return the number


def fizzbuzz(x):
    if (x % 3 == 0) and (x % 5 == 0):
        return 'FizzBuzz'
    elif x % 3 == 0:
        return 'Fizz'
    elif x % 5 == 0:
        return 'Buzz'
    else:
        return x

foo = 5
bar = 0
try:
    baz = foo / bar
    print ("The answer is %d" % baz)
except ZeroDivisionError:
    print ('You tried to divide by zero')
print ('End script')

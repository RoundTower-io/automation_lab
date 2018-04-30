def myFunction():
    return

def changeme(mylist, addition):
   mylist.append(addition)
   return mylist

def printme(numberlist):
    print ('Values in the list {0}'.format(numberlist))
    return

numberlist = [10,20,30]
printme (numberlist)
numberlist = changeme(numberlist, 99)
printme (numberlist)
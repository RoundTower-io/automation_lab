def myFunction():
    return


def changeme(mylist, addition):
    mylist.append(addition)
    return mylist


def printme(numberlist):
    for num in numberlist:
        print("number: %d" % num)
    return


numberlist = [10, 20, 30]
printme(numberlist)
numberlist = changeme(numberlist, 99)
printme(numberlist)

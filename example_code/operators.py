x = 13
y = 10
z = 10
message = 'This is a message'

print(x * y) #130
print(x % y) #3
print(x is message) #False
print(y == z) #True
print(y == z and y is z) #True
print(message is not None) #True

message = 'Hello'
print(message + ' there!') #Hello there!
print(message*3) #HelloHelloHello
print(message[1]) #e
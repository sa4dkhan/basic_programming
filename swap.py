x = int(input("First number: "))
y = int(input("Second number: "))
'''
temp = x
x = y
y = temp
'''
'''
x = x + y
y = x - y
x = x - y
'''

x = x * y
y = x / y
x = x / y

print("The value of first number after swapping: {}".format(x))
print("The value of second number after swapping: {}".format(y))
# EXERCISES
# Print the type of 42, 3.14, and 'hello'.

# print(type(42))
# print(type(3.12))
# print(type('helloo'))

# Convert a string '100' to an integer.
string = int('100')
# print(type(string))

# Add an integer and a float together. What is the result?
x = 3
y = 3.14
addition = x + y
# print(addition)
# What happens when you try to multiply a string by a number?
z = 'anitah'
multi = z * x
# print(multi)

# CHALLENGE
# Write a program that:
# Asks the user to enter two numbers (as strings)
num1 = input('Enter the first number as a string:')
num2 = input('Enter the second number as a string:')
# Converts them to integers or floats
num1 = int(num1)
num2 = float(num2)
# Prints their sum and type
result = num1 + num2
print(result)
print(type(result))
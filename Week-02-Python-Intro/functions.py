# EXERCISES
# Write a function greet(name) that prints “Hello, [name]”.
# def greet (name):
#     print(f'Helloo {name}')
# greet('Anitah')
# Create a function add(a, b) that returns the sum.
# Modify add() to print “even” or “odd” based on the result.
# def add(a, b):
#     result= a + b
#     print(f'Sum: {result}')
#     if result % 2 ==0:
#         print('The result is even.')
#     else:
#         print('The result is odd.')
# add(10, 27)

# Call a function from within another function.
# def func1(): # outer function
#     info = "Anitah and Anitah only"
    
#     def func2(): # inner function
#         print(info)  # accessing outer function's variable
    
#     func2()
# func1()

# CHALLENGE
# Write a calculator function:
# Takes two numbers and an operation (+, -, *, /)
# Returns the result
def calculation(x, y):
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        if y != 0:
            return x / y
        else:
            return "Oopsy😁,you can't divide by zeroo"
    else:
        return "Giirllll please!😏"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

result = calculation(num1, num2)
print(f"Result: {result}")
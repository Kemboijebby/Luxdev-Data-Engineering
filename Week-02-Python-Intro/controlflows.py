# Write a program that checks if a number is positive, negative, or zero.
# Ask the user to enter a number
num = float(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")
    
# Create a program that checks if someone is eligible to vote.
age = int(input('Enter your age:'))
citizenship = input("What is your citizenship? ").strip().lower()
if age >= 18 and citizenship == "kenyan":
    print('You are eligible to vote.')
elif age < 18 and citizenship == "kenyan":
    print('You still young to vote')
elif age >= 18 and citizenship != "kenyan":
    print('Non-citizens are not eligible to vote')
else:
    print("You are not eligible to vote.")


# Write a program that takes 3 numbers and prints the largest one.
# Get 3 numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
largest = max(num1, num2, num3)
print(f"The largest number is: {largest}")

# Practice combining and, or, not.
# CHALLENGE
# Build a grading system:
# Input score (0–100)
# Output grade: A (90+), B (80–89), et
score = float(input('Enter the student score:'))
if score >= 90:
    print('Grade: A')
elif score >= 80:
    print('Grade: B')
elif score >= 70:
    print('Grade: C')
else:
    print('Grade: D')

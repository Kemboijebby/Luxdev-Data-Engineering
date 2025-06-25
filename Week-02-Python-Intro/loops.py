# EXERCISES
# Use a for loop to print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# Use a while loop to print numbers until the user enters stop.
while True:
    myinput = input("Enter something (type 'stop' to end): ")
    if myinput.lower() == 'stop':
        break
    print(myinput)


# Write a loop that prints even numbers from 1 to 20.
for i in range(1,21):
    if i % 2 == 0:
      print(i)
       
# Explain what break and continue do in your own words.
    #  Continue- Skips current iteration, continues to next
    #  Break - Stops the loop entirely


# CHALLENGE
# Write a guessing game that asks the user to guess a secret number between 1 and 10.
# Give feedback (too high / too low)
# Use a while loop
import random
secret_number=random.randint(1, 10)
user_input = int(input('Guess a number between 1 to 10:'))
while True:
   if user_input > secret_number:
      print(f'Too high, secret number is:{secret_number}')
      break
   elif user_input < secret_number:
      print(f'Too low, secret number is:{secret_number}')
      break
   else:
      print('Got it')
      break
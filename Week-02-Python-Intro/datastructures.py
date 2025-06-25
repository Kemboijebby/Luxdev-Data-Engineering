# EXERCISES
# Create a list of 5 fruits and print the third fruit.
fruits = ['Apples','Mangoes','Bananas','Berries','Lemons']
# print(fruits[2])
# Create a dictionary with keys: name, age. Print the value of age.
details = {'Name':'Anitah',
           'Age':'23',
           'city':'Nairobi'}
# print(details['Name'])

# Define a tuple with three numbers. Try modifying it. What happens?
numbers = (1,2,3,4,5)
numbers[3]=10  #error
print(numbers)

# Create a set from a list with duplicate values.
mylist =[1, 2, 2, 3, 4, 4, 5, 5, 5]
unique = set(mylist)
print(unique)

# CHALLENGE
# # Step 1: Create an empty list
user_inputs = []

# Step 2: Take 5 user inputs
for i in range(5):
    item = input(f"Enter item {i + 1}: ")
    user_inputs.append(item)

# Step 3: Convert the list to a set to remove duplicates
unique_values = set(user_inputs)

# Step 4: Print the unique values
print("\nUnique values:")
print(unique_values)

# Task 1: List Comprehension – Student Grades
# You are given a list of student scores:
scores = [45, 78, 88, 56, 90, 62, 33, 99, 70, 50]
# Instructions:

# Use a list comprehension to filter all the scores above 60 and store them in a new list called passed.
scores_filter =[s for s in scores if s > 60 ]
print(scores_filter)

# Use another list comprehension to convert all scores into "Pass" or "Fail" using a threshold of 50.
result = ["Pass" if s > 50 else "Fail" for s in scores]

print(result)

# Task 2: Dictionary Comprehension – Student Report
# You are given two lists:

students = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
marks = [82, 48, 79, 65, 91]
# Instructions:

# Create a dictionary using comprehension that pairs each student with their mark.
result = {k:v for (k,v) in zip(students,marks)}
print(result)

# Create a second dictionary that stores only students who scored more than 70
passed_students= {k:v for (k,v) in zip(students,marks)if v > 70}
print(passed_students)

# Create a third dictionary that maps each student to "Pass" or "Fail" (threshold: 50).
result2 = {k: "Pass" if v > 50 else "Fail" for k, v in zip(students, marks)}
print(result2)

# Bonus Challenge (for advanced learners)
# Given a sentence:
sentence = "Data science is fun and insightful"
# Write a dictionary comprehension that maps each word to its length
result3 = {s: len(s) for s in sentence.split()}
print(result3)
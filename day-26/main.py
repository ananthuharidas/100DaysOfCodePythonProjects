"""List Comprehension"""
list = [1, 2, 3]
new_list = [n+1 for n in list]
print(new_list)

name = "Ananthu"
new_list = [letter for letter in name]
print(new_list)

new_list = [number * 2 for number in range(1, 5)]
print(new_list)
"""List Comprehension"""
# Syntax new_list = [new_item for item in list if test]
# Example create new list by selecting only names with more than 5 letters and turn it into uppercase

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
new_list = [name.upper() for name in names if len(name) > 5]
print(new_list)

import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_score = {student: random.randint(1, 100) for student in names}
print(students_score)
passed_students = {student: score for (student, score) in students_score.items() if score >= 60}
print(f"Passed Students: {passed_students}")
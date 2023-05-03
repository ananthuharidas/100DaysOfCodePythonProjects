student_dict = {
    "student": ["Angela", "James", "Ashley"],
    "score": [96, 49, 75]
}
# Looping through dictionary
for (key, value) in student_dict.items():
    print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of the data frame using iterrows
for (index, row) in student_data_frame.iterrows():
    # Print entire row
    print(row)
    # Or Print the student name only
    print(row.student)
    # Or print the score only
    print(row.score)
    # Or print row with a particular name
    if row.student == "Angela":
        print(row.score)

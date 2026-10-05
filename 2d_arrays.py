students_2d = [
    ["Charles", 15],
    ["Ngotho", 16],
    ["Kamande", 17],
    ["Emryn", 18],
    ["Waringa", 19]
]

print("MY SAMPLE 2D ARRAY")
print(students_2d)


# for an edit, we access the specific index of the 2d array and change to the new value
students_2d[0][1] = 21

print("\nAFTER EDITING CHARLES AGE")
print(students_2d)


# for the addition, we used the append method to add a new name to the 2d array
students_2d.append(["Doreen", 23])

print("\nAFTER ADDING Doreen")
print(students_2d)


# For a delete, we used the del keyword and specify the index of the 2d array to delete
del students_2d[5]

print("\nAFTER DELETING Doreen")
print(students_2d)
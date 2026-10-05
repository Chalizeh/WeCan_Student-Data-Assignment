# My Sample 3D ARRAY

students_3d = [
    [
        ["Charles", 20],
        ["Ngotho", 21]
    ],

    [
        ["Kamande", 22],
        ["Emryn", 20]
    ],

    [
        ["Waringa", 21],
        ["Doreen", 23]
    ]
]


print("My Sample 3D ARRAY")

for group in students_3d:
    print(group)


# for an edit, we access the specific index of the 3d array and change to the new value
students_3d[0][0][1] = 21

print("\nAFTER EDITING CHARLES AGE")
print(students_3d)


# for the addition, we used the append method to add a new name to the 3d array
students_3d[0].append(["Kennedy", 24])

print("\nAFTER ADDING KENNEDY")
print(students_3d)


# For a delete, we used the pop method to remove the last element from the 3d array
students_3d[0].pop()

print("\nAFTER DELETING KENNEDY")
print(students_3d)
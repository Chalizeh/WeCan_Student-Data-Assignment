#This is list of my students and their ages by charles_Admin_1016

students = ["Charles", "Ngotho", "Kamande", "Emryn", "Waringa"]

ages = [15, 16, 17, 18, 19]

print("CURRENT STUDENT AGES")

for i in range(len(students)):
    print(students[i], "is", ages[i], "years old")

#This is a list of my students ages in two years by Charles_Admin_1016
ages_in_two_years = []

for age in ages:
    ages_in_two_years.append(age + 2)


print("\nAGES IN TWO YEARS")

for i in range(len(students)):
    print(students[i], "will be", ages_in_two_years[i], "years old")



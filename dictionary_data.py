students = {
    "Charles": {
        "age": 20,
        "date_of_birth": "31/05/2000",
        "location": "Dandora",
        "admission_number": "ADM1016"
    },

    "Ngotho": {
        "age": 21,
        "date_of_birth": "10/03/2005",
        "location": "Kayole",
        "admission_number": "ADM1017"
    },

    "Kamande": {
        "age": 22,
        "date_of_birth": "20/01/2004",
        "location": "Mwiki",
        "admission_number": "ADM1018"
    },

    "Emryn": {
        "age": 20,
        "date_of_birth": "12/07/2006",
        "location": "Umoja",
        "admission_number": "ADM1019"
    },

    "Waringa": {
        "age": 21,
        "date_of_birth": "25/09/2005",
        "location": "Githurai",
        "admission_number": "ADM1020"
    }
}

for name, data in students.items():

    print("\nStudent Name:", name)
    print("Age:", data["age"])
    print("Date of Birth:", data["date_of_birth"])
    print("Location:", data["location"])
    print("Admission Number:", data["admission_number"])

students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]

# How many students are there?
print (f" There are {len(students)} students")

# How many students prefer light coffee? For each type of coffee roast?
coffee_pref = 0
for student in students:
    if student['coffee_preference'] == 'light':
        coffee_pref += 1
print(f"There are {coffee_pref} students who prefer light coffee")

# How many types of each pet are there?
pet_species = []
for student in students:
    for pet in student['pets']:
        pet_species.append(pet['species'])
print(f"The number of horses is: {pet_species.count('horse')}")
print(f"The number of dogs is: {pet_species.count('dog')}")
print(f"The number of cats is: {pet_species.count('cat')}")

# How many grades does each student have? Do they all have the same number of grades?
num_of_grades = 0
amount_of_grades = 0
for student in students:
    amount_of_grades = len(student['grades'])
    if amount_of_grades > num_of_grades:
        num_of_grades = amount_of_grades
print(f"There are {num_of_grades} grades for each student")


# What is each student's grade average?
for student in students:
    avg = sum(student['grades'])/len(student['grades'])
    print(f"The average grade for {student['student']} is {round(avg,2)}")

# How many pets does each student have?
i = 0
for student in students:
    print(f"The number of pet(s) {student['student']}  have/has is {len(students[i]['pets'])}")
    i += 1

# How many students are in web development? data science?
wd = 0
ds = 0
for student in students:
    if student['course']  == 'web development':
        wd += 1
    elif student['course'] == 'data science':
        ds += 1
print(f"The number of students in web development are: {wd}")
print(f"The number of students in data science are: {ds}")

# What is the average number of pets for students in web development?
number_of_pets = []
for student in students:
    if student['course'] == 'web development':
        number_of_pets.append(len(student['pets']))
print(f"The average number of pets of students in web development is: {(round(sum(number_of_pets) / len(number_of_pets), 2))}")


# What is the average pet age for students in data science?
ages_of_pets = []
for student in students:
    if student['course'] == 'data science':
        for pet in student['pets']:
            ages_of_pets.append(pet['age'])
print(f"The average age of pets owned by data science students is: {round(sum(ages_of_pets) / len(ages_of_pets), 2)}")

# What is most frequent coffee preference for data science students?
coffee_preferences = []
for student in students:
    if student['course'] == 'data science':
        coffee_preferences.append(student['coffee_preference'])
print(f"The most common coffee preferred by data science students is: {max(set(coffee_preferences))}")

# What is the least frequent coffee preference for web development students?
coffee_preferences = []
for student in students:
    if student['course'] == 'web development':
        coffee_preferences.append(student['coffee_preference'])
print(f"The least common coffee preferred by web development students is: {min(set(coffee_preferences))}")

# What is the average grade for students with at least 2 pets?
list_of_grades = []
final_list_of_grades = []
for student in students:
    if len(student['pets']) >= 2:
        list_of_grades.append(student['grades'])
for item in list_of_grades:
    final_list_of_grades += item
print(f"The average grade for students with at least two pets is: {round(sum(final_list_of_grades) / len(final_list_of_grades), 2)}")

# How many students have 3 pets?
number_of_pets = []
for student in students:
    number_of_pets.append(len(student['pets']))
print(f"The number of students having 3 pets is: {number_of_pets.count(3)}")

# What is the average grade for students with 0 pets?
list_of_grades = []
final_list_of_grades = []
for student in students:
    if len(student['pets']) == 0:
        list_of_grades.append(student['grades'])
for item in list_of_grades:
    final_list_of_grades += item
print(f"The average grade for students with no pets is: {round(sum(final_list_of_grades) / len(final_list_of_grades), 2)}")

# What is the average grade for web development students? data science students?
web_development_grades = []
final_list = []
for student in students:
    if student['course'] == 'web development':
        web_development_grades.append(student['grades'])
for item in web_development_grades:
    final_list += item
print(f"The average grade of web development students is: {round(sum(final_list) / len(final_list), 2)}")

data_science_grades = []
final_list = []
for student in students:
    if student['course'] == 'data science':
        data_science_grades.append(student['grades'])
for item in data_science_grades:
    final_list += item
print(f"The average grade of data science students is: {round(sum(final_list) / len(final_list), 2)}")

# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
list_of_grades = []
final_list_of_grades = []
for student in students:
    if student['coffee_preference'] == 'dark':
        list_of_grades.append(student['grades'])
for item in list_of_grades:
    final_list_of_grades += item
print(f"The grades of dark coffee drinkers range from: {min(final_list_of_grades)} to: {max(final_list_of_grades)}")

# What is the average number of pets for medium coffee drinkers?
number_of_pets = []
for student in students:
    if student['coffee_preference'] == 'medium':
        number_of_pets.append(len(student['pets']))
print(f"The average number of pets for medium coffee drinkers is: {round(sum(number_of_pets) / len(number_of_pets), 2)}")

# What is the most common type of pet for web development students?
pet_species = []
for student in students:
    if student['course'] == 'web development':
        for pet in student['pets']:
            pet_species.append(pet['species'])
print(f"The most common pet species of web development students are: {max(set(pet_species))}")

# What is the average name length?
lengths_of_names = []
for student in students:
    lengths_of_names.append(len(student['student']))
print(f"The average name length is: {round(sum(lengths_of_names) / len(lengths_of_names), 2)}")

# What is the highest pet age for light coffee drinkers?
ages_of_pets = []
for student in students:
    if student['coffee_preference'] == 'light':
        for pet in student['pets']:
            ages_of_pets.append(pet['age'])
print(f"The highest pet age for light coffee drinkers is: {max(set(ages_of_pets))}")
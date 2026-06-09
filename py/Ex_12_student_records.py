#Create a dictionary called students_records with the following information: "student_001":name is "John", age is 19, major is "Computer Science", grades are [85,92,78] "student_002": name is "Sarah", age is 20, major is "Biology", grades are [90,88,95]

students_records = { 
    "student_001": 
        {"name":"John",
         "age":19,
         "major":"Computer Science",
         "grades":[85,92,78]
        },
    "student_002": 
        {"name":"Sarah",
         "age":20,
         "major":"Biology",
         "grades": [90,88,95]
        }, # Add a new student "student_003" with name "Mike", age 18, major "Math", grades [82,79,91]
    "student_003": 
        {"name":"Mike",
         "age":18,
         "major":"Math",
         "grades": [82,79,91]
        }
}

keys = students_records.keys()

print (keys)


#Update John's age to 20 

students_records["student_001"]["age"] = 20

print(students_records["student_001"])

# Loop through the dictionary and print each students information in this format:"Student ID: [id], Name:[name], Major:[major]"

for student_id, info in students_records.items():
    print(f"Student ID: {student_id}, Name: {info['name']}, Major: {info['major']}")
#Create a system that stores student grades as tuples (name,subject,grade) and uses sets to find unique subjects and students 

grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95),
]

students = set() # - empty set to store student name

for grade in grades: 
    students.add(grade[0])
print ("Unique students:", students)


subjects = set() # - empty set to store unique subject 

for name, subject, grade in grades:  # - to loop through each tuple 
    students.add(name)
    subjects.add(subject)


print ("Students:", students)
print ("Subjects:", subjects)
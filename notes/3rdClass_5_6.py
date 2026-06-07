#List - A list is a collection of items that are ordered and mutable (changeable). Lists are created using square brackets [].

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty_list = []

#Accessing Elements 
print(fruits[0])  # Output: apple
print(fruits[-1])  # Output: cherry
print(numbers[1:4])  # Output: [2, 3, 4]
print(numbers[:3])    # Output: [1, 2, 3]
print(numbers[2:])    # Output: [3, 4, 5]

#print(empty_list[0])  # This will raise an IndexError since the list is empty


#Lists Operations - CRUD a list 

fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]   
mixed = ["hello", 42, 3.14, True]
empty_list = [] 

fruits.append("orange")  # Add an item to the end of the list

fruits.insert(1, "grape")  # Insert an item at a specific index

fruits.remove("banana")  # Remove an item by value  

popped = fruits.pop()  # Remove and return the last item

fruits.sort()  # Sort the list in ascending order

fruits.reverse()  # Reverse the order of the list


# #List operations 
len(fruits)  # Get the number of items in the list
#"apple" in fruits  # Check if an item is in the list
# fruits + ["kiwi", "melon"]  # Concatenate two lists
# fruits * 2  # Repeat the list

print(len(fruits))


print(fruits)


#Tuples -  a set of data within parentheses 

coordinates = (10,20)

person = ("Alice", 25, "Engineer")

single_item = (42,)

#Tuple operations 

print(coordinates[0]) 
print(len(person))


#Sets - a set of data within curly bracket

fruits = {"apples", "banana", "orange"}

numbers = {1,2,3,4,5}

#Set operations 

fruits.add("grape")
fruits.remove("banana")
fruits.discard("kiwi")

print(fruits)

set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))


#dictionaries 

student = { 
    "name" : "Alice", 
    "age"  : 20, 
    "grade": "A",
}

# Accessing and modifying 

print(student["name"])
print(student.get("age"))
student["age"] = 21
student["email"] = "alice@gmail.com" 

#Dictionaris method 

keys = student.keys()
values = student.values()
items = student.items()

print(keys)
print(values)
print(items)

#Iterating Dictionaries 

#Iterating through dictionaries 

for key in student: 
    print (f'{key}: {student[key]}')

for key,value in student.items():
    print(f"{key}: {value}")

#Nested dictionaries 

company = {
    "employees" : {
        "john": {"age": 30, "department": "IT"}, 
        "jane": {"age": 25, "department": "HR"}
    }, 
    "departments" : ["IT", "HR", "Finance"]
}

print (company["employees"].items())
print(company["departments"])


#Functions 

#Functions with parameters

def greet_person(name):
    print(f"Hello,{name}!")

greet_person("Alice")

#Functions with return values 

def add_numbers(a,b): 
    return a + b 

result = add_numbers(5,3)
print (result)

#Default parameters

def greet_with_title(name, title="Mr."):
    return f"Hello,{title} {name}!"

print(greet_with_title("Smith"))
print(greet_with_title("Johnson","Dr."))


#Agrs 

#Agrs - varible number of arguments 

def sum_all(*args):
    return sum(args)
print(sum_all(1,2,3,4,5))

#kwards - keyword arguments 

def print_info(**kwargs): 
    for key, value in kwargs.items(): 
        print (f"{key}: {value}")
print_info(name="Alice", age=25, city="New York")

#args&kwargs 

#combining * args and **kwargs 

def flexible_function(*args, **kwargs):
    print("Positional arguements", args)
    print("Keyword arguements:", kwargs)
flexible_function(1,2,3, name="Alice", age=25)

#Lambda 

#Lambda functions (anonymous functions) 

square = lambda x: x**2 
print(square(5))

add = lambda x, y: x + y 
print(add(3, 4))
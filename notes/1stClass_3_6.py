
#Variables are used to store data that can be used later in the program. They are created by assigning a value to a name. The name can be any valid identifier, and the value can be of any data type.

#Data types are the different types of values that can be stored in a variable. The most common data types in Python are:

name = 'Jacquelina' #String # this is a variable that holds a string value
age = 30      #Integer # this is a variable that holds an integer value
weight = 65.5   #Float # this is a variable that holds a float value
is_student = True  #Boolean # this is a variable that holds a boolean value


print (name) # this will print the value of the variable 'name'
print (age) # this will print the value of the variable 'age'      
print (weight) # this will print the value of the variable 'weight'
print (is_student) # this will print the value of the variable 'is_student'


# Math operations with variables

x = 10
y = 5

Additon = x + y
Subtraction = x - y
Multiplication = x * y
Division = x / y
Floor_Division = x // y
Modulus = x % y
Exponentiation = x ** y

print (Additon) # this will print the result of x + y
print (Subtraction) # this will print the result of x - y
print (Multiplication) # this will print the result of x * y
print (Division) # this will print the result of x / y
print (Floor_Division) # this will print the result of x // y
print (Modulus) # this will print the result of x % y
print (Exponentiation) # this will print the result of x ** y

#String Manipulation

#String Creation and Concatenation
single_quote_string = 'Hello, World!' # this is a string created using single quotes
double_quote_string = "Hello, World!" # this is a string created using double quotes
triple_quote_string = """Hello, World!
I am Jacquelina """ # this is a string created using triple quotes

print (single_quote_string) # this will print the value of the variable 'single_quote_string
print (double_quote_string) # this will print the value of the variable 'double_quote_string'
print (triple_quote_string) # this will print the value of the variable 'triple_quote_string'

#string Indexing and Slicing

text = "Python Programming"
print (text[0]) # this will print the first character of the string 'text'
print (text[7]) # this will print the eighth character of the string 'text'
print (text[-1]) # this will print the last character of the string 'text'
print (text[:6]) # this will print the first six characters of the string 'text'
print (text[7:]) # this will print the characters from index 7 to the end of the string


#string methods

name = "Jacquelina Stanley"
print (len(name)) # this will print the length of the string 'name'
print (name.strip()) # this will remove any leading or trailing whitespace from the string 'name'
print (name.upper()) # this will print the string 'name' in uppercase letters
print (name.lower()) # this will print the string 'name' in lowercase letters
print (name.replace("Jacquelina", "Shalinie")) # this will replace the substring "Jacquelina" with "Shalinie" in the string 'name'
print (name.split()) # this will split the string 'name' into a list of words

#string formatting

age = 30
name = "Jacquelina"

message = f"My name is {name} and I am {age} years old." # this will create a formatted string using the format method
print (message) # this will print the value of the variable 'message'

#Github 1st repo 
echo "# Python-Bootcamp" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/jacquelinastanley/Python-Bootcamp.git
git push -u origin main


#Github update repo 

git remote add origin https://github.com/jacquelinastanley/Python-Bootcamp.git
git branch -M main
git push -u origin main



git add .
git commit -m "comment"
git push


#cd.. 

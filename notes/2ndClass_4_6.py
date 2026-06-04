#Input Output Validation
# 
#

name = input("Enter your name: ") # this will prompt the user to enter their name and store it in the variable 'name'
height = float(input("Enter your height: ")) # this will prompt the user to enter their height and convert it to a float


#Input Validation

while True:
    try:
        age = int(input("Enter your age: ")) # this will prompt the user to enter their age and convert it to an integer
        if age > 0: 
            break 
        else: # this will check if the input is a negative number
            print("Age cannot be negative. Please enter a valid age.") # this will print an error message if the input is invalid
    except ValueError: # this will catch the ValueError if the input cannot be converted to an integer
        print("Invalid input. Please enter a valid age.") # this will print an error message if the input is invalid

#Output Validation 

print (f"Hello, {name}! Your height is {height} and your age is {age}.") # this will print a formatted string with the user's name, height, and age


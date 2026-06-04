#Input Output Validation
# 
#

name = input("Enter your name: ") 

height = float(input("Enter your height: "))


#Input Validation

while True:
    try:
        age = int(input("Enter your age: ")) 
        if age > 0: 
            break 
        else: 
            print("Age cannot be negative. Please enter a valid age.") 
    except ValueError: 
        print("Invalid input. Please enter a valid age.")


#while true - this will create an infinite loop that will continue until a valid age is entered. The loop will only break when the user enters a valid age that is greater than 0.

#try-except - this will allow the program to handle errors gracefully without crashing. If the user enters an invalid input that cannot be converted to an integer, the except block will catch the error and prompt the user to enter a valid age.

#if statement - this will check if the age entered by the user is greater than 0. If it is, the loop will break and the program will continue. If it is not, an error message will be printed and the loop will continue until a valid age is entered.

#else statement - this will provide feedback to the user if they enter a negative age, prompting them to enter a valid age.

#break statement - this will exit the loop once a valid age is entered, allowing the program to continue with the rest of the code.


#Output Validation 

print (f"Hello, {name}! Your height is {height} and your age is {age}.") # this will print a formatted string with the user's name, height, and age


#Conditional Statements 

#Operators 
# = Assignment 
# == Equal to
# === Strict equality 
# != Not equal to
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to


#if-eles: 2 conditions
#if-elif-else: multiple conditions


age = 18
if age >= 18:
    print("You are an adult.")   
else:
    print("You are a minor.")

score = 85
if score >= 90:
    print("Grade: A")   
elif score >= 80:
    print("Grade: B")   
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

print(f"Your final grade is: {score}.") # this will print the final grade based on the score


#and - both conditions must be true
#or - at least one condition must be true

user_age = 25
has_license = True

if user_age >= 18 and has_license:
    print("You can drive.") 
else:
    print("You cannot drive.")


day = input("Enter day of the week: ")
if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

#Nested condition - a condition inside another condition

weather = "sunny"
temperature = 30

if weather == "sunny":
    if temperature > 70: 
        print ("It's a hot sunny day.")
    else:
        print ("It's a nice sunny day.")
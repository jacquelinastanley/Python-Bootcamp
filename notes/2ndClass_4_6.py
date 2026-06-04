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



if age > 18:
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


has_license = True

if age >= 18 and has_license:
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


#Loops 

#for loop - iterates over a sequence (like a list, tuple, or string) and executes a block of code for each item in the sequence.    
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # this will print each fruit in the list 'fruits'

for i in range(5):
    print(i) # this will print the numbers from 0 to 4
for i in range(1, 6):
    print(i) # this will print the numbers from 1 to 5
for i in range(0, 10, 2):
    print(i) # this will print the even numbers from 0 to 8

#while loop - executes a block of code as long as a specified condition is true.
count = 0
while count < 5:
    print(count) # this will print the current value of 'count'
    count += 1 # this will increment the value of 'count' by 1 in each iteration of the loop

#Loops control statements

for i in range(10):
    if i == 3:
        continue
    if i == 5:
        break # this will exit the loop when i is equal to 5
    print(i) # this will print the numbers from 0 to 4


#Nested loops - a loop inside another loop

for i in range(2):
    for j in range(3):
        print(f"i: {i}, j: {j}") # this will print the values of i and j for each iteration of the nested loops 
    
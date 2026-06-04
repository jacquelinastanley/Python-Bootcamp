#Create a simple calculator that takes two numbers and an operation from user 


first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))   
operation = input("Enter the operation (+, -, *, /): ") 

if operation == "+":
    result = first_number + second_number       
elif operation == "-":
    result = first_number - second_number   
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."
print("Result:", result)

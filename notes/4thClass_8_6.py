
# #Error Handling - process olf anticipating , catching and managing errors that occur during program execution 



# #Basic exception handling 

try: 
    number = int(input("Enter a number: "))
    result = 10 / number 
except ValueError:
    print ("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print ("Cannot divide by zero")

# #Using else and finally 

try: 
    file = open("data.txt", "r")
except FileNotFoundError:
    print ("File not found!")
else: 
    #Executes if no exception occured 
    content = file.read()
    print("File read successfully")
finally: 
    #Always execute 
    if 'file' in locals() and not file.closed: 
        file.close()
    print("Cleanup completed")

# #Raising exceptions 

def validate_age(age):
    if age < 0: 
        raise ValueError("Age cannot be negative")
    if age > 150: 
        raise ValueError("Age seems unrealistic")
    return True 

try: 
    validate_age(-5)
except ValueError as e: 
    print(f"Validation error :{e}")

#Classes and Objects 

#Classes - a big box with multiple small box 


#Basic class definition 
class Person: 
    # Class attribute (shared by all instances)
    species = "Human"

    #Constructor method 
    def __init__(self, name, age):
    #Instance attributes 
        self.name = name 
        self.age = age

    #Instance method 
    def introduces(self): 
        return f"Hi,I'm {self.name} and I'm {self.age} years old"

    #Method with parameters 
    def have_birthday(self):
        self.age += 1 
        return f"Happy birthday! {self.name} is now {self.age}"

#Creating objects (instances)
person1 = Person("Alice",25)
person2 = Person("Bob",30)

#Accessing attributes 
print(person1.name) #Alice 
print(person1.age)

#Calling methods 
print(person1.introduces())
print(person1.have_birthday())

#Class attributes 
print(Person.species)
print(person1.species)

#_inti_ to prevent repetition 

class BankAccount: 
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner 
        self.balance = balance 
        self.transaction_history = []
    
    def deposite(self,amount):
        if amount > 0: 
            self.balance += amount 
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else: 
            return "Invalid deposit amount"
        
    def withdraw(self, amount): 
        if amount > 0 and amount <= self.balance: 
            self.balance -= amount 
            self.transaction_history.append(f"Withdraw #{amount}")
            return f"Withdraw ${amount}. New balance: ${self.balance}"
        else: 
            return "Invalid withdrawal amount or insufficient funds"
   
    def get_balance(self):

        return f"Current balance: ${self.balance}"
    
    def get_transaction_history(self): 
        return self.transaction_history
    
account = BankAccount("12345", "Alice", 0)
print (account.deposite(600))
print (account.withdraw(200))
print (account.get_balance())
print (account.get_transaction_history())

#OOP

#inheritance - pass parent class into child 

#inheritance 

# class Shape: #Parent class 
#     def __init__(self,name):
#         self.name = name 
    
#     def area(self):
#         return 0 
    
# class Circle(Shape): # Child inherits from Shape 
#     def __init__(self,radius):
#         super().__init__("Circle")
#         self.radius = radius 
    
#     def area(self): #Override parent method 
#         return 3.142 * self.side * self.side 

# class Square(Shape): # Child inherits from Shape 
#     def __init__(self,side):
#         super().__init__("Square")
#         self.side = side 
    
#     def area(self): #Override parent method 
#         return 3.142 * self.side * self.side 
    
# #Both Circle and Square inherit 'name' attribute from Shape 
# circle = Circle(5)
# square = Square(4)

# print(circle.name)
# print(square.name)

# #Polymorphism 

# def print_area(shape): 
#     print(f"{shape.name} area:{shape.area()}")

# #Same method call, different behaviors 

# print_area(circle)
# print_area(square)

# #Or with a list 
# shapes = [Circle(3), Square(5), Circle(2)]
# for shape in shapes:
#     print_area(shape)

# Modules 

from math_utils import add, multiply, factorial, PI, Calculator

result = add(5,3)
print (f"Additional Result: {result}")

result = multiply(5,3)
print (f"Multiply Result: {result} ")


#Libraries 

import os 
import sys
import datetime
import random 

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print (f"Now date: {now}")
print (f"Today's Date: {today}")
print (f"Current Date and Time: {formatted_date}")

random_number = random.randint(1,100)
random_choice = random.choice(['apple','banana','orange'])
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(f'Random Number: {random_number}')
print(f'Random Choice: {random_choice}')
print(f'Shuffled List: {numbers}')

        
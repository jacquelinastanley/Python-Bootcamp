#Create a multiplication table generator 

for i in range(1, 11):
    print(f"Multiplication Table for {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print() # this will print a blank line after each multiplication table  
    
# Build a temperature converter function (Celsius to Fahrenheit)

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius *9/5) + 32
    return fahrenheit 

temp = float(input("Enter temperature in Celsius: "))
print("Fahrenheit:", celsius_to_fahrenheit(temp))
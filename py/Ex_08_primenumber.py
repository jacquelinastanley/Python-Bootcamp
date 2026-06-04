# Write a program that finds all prime numbers up to a given number (limit=20)


limit = 20  

for num in range(2, limit + 1):
    is_prime = True
    for divisor in range(2, int(num**0.5) + 1):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

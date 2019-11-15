def fibonacci(max_n):
    a = 0
    b = 1
    total = 0
    new_number = 0
    while new_number < max_n:
        new_number = a + b
        if new_number % 2 == 0:
            total += new_number
        a, b = b, new_number
    return total
    
print(fibonacci(4000000))

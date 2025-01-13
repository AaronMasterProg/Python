# Numeros primos - como encontrarlos

def is_prime(num):
    a=int(1 + num ** 0.5)
    for i in range(2, a):
        if num % i == 0:
            return False                    
    return True

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

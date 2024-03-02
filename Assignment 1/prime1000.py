def isPrime(number):
    if number == 0 or number == 1:
        return False
    
    for i in range(2,number):
        if number%i == 0:
            return False

    return True


for i in range(1, 1001):
    if isPrime(i):
        print(i, end=" ")

print()

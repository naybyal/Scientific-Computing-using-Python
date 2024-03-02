def fact(number):
    factorial = 1
    if number == 1 or number == 0:
        factorial *= 1
    else:
        factorial *= number * fact(number-1)

    return factorial

n = int(input('Enter n : '))
r = int(input('Enter r : '))

# nPr = n! / (n-r)!
# nCr = nPr / r!

p = fact(n)/fact(n-r)
c = p/fact(r)

print("nPr :", p)
print("nCr :", c)
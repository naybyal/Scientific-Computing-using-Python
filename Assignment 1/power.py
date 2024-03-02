# pow(x,y) w/out using library functions

def compute_power(base, exponent):
    result = 1
    while exponent != 0:
        result *= base
        exponent -= 1
    return result

print("-- POW(X,Y) --")
base = int(input("Reading base... "))
exponent = int(input('Reading exponent... '))

print('Result :', compute_power(base, exponent))

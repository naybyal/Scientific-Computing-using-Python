def square(n):
    return n**2

print(square(2))

def average(list):
    sum = 0
    for element in list:
        sum += element
    return sum/len(list)

list = [5,10,15,20,25]
print(average(list))

#   boolean functions   ->  return boolean values

def odd(n):
    return n%2 != 0 

print(odd(5))
print(odd(6))
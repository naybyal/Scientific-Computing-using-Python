def square(n):
    return n**2

print(square(2))

def average(list):
    sum = 0
    for element in list:
        sum += element

    return sum/len(list)

list = [1,2,3,4,5]
print(average(list))
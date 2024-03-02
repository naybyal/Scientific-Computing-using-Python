def count_even(array):
    evenCount = 0
    for element in array:
        if element%2 == 0:
            evenCount+=1
    
    return evenCount


totalElements = int(input("Total no. of elements : "))
elements = []
print("Reading array elements...")
for i in range(totalElements):
    addToList = int(input())
    elements.append(addToList)

evenCount = count_even(elements)
oddCount = totalElements - evenCount

print('Even Count :', evenCount)
print('Odd Count :', oddCount)
#   mutable object
#       internal state of the object can be changed


#   append, extend

first = [10, 20, 30]

second = first      # aliasing effect
print(first)

first[1] = 99
print(first)
print(second)


first = [20,30,40]
second = first
third = [20,30,40]

print(first == second)
print(first == third)   # values are the same hence true.
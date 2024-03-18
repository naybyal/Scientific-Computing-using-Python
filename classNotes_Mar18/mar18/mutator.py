#   mutable object
#       internal state of the object can be changed


#   append, extend

first = [10, 20, 30]

second = first
print(first)

first[1] = 99
print(first)
print(second)

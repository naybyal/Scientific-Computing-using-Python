rows = int(input('Row count (not greater than 26) : '))

if rows <= 26 and rows > 0:
# A --ASCII VALUE--> 65
    for i in range(1, rows+1):
        start = 65
        for j in range(i):
            alphabet = chr(start)
            print(alphabet, end=" ")
            start += 1
        print()
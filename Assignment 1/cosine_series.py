PI = 3.142;   

def cosXSeriesSum(x, n):       
    # here x is in degree. 
    # we have to convert it to radian  
    # for using it with series formula,  
    # as in series expansion angle is in radian 
    x = x * (PI / 180.0);  
    res = 1; 
    sign = 1;  
    fact = 1; 
    pow = 1; 
    for i in range(1,5): 
        sign = sign * (-1); 
        fact = fact * (2 * i - 1) * (2 * i); 
        pow = pow * x * x; 
        res = res + sign * pow / fact; 
    return res;  
  
x = int(input("Enter the value of x in degrees: ")) 
# n = int(input("Enter the number of terms: ")); 
print(round(cosXSeriesSum(x, 10), 6)); 
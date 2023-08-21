def extraLongFactorials(n):
    prod = 1
    for i in range(2, n):
        prod = prod*i
    prod = prod*n
    print(prod)



# In languages like C/C++, such big integers are not handled. So we must create a new class BigInt, 
# and override operators to handle such big integers
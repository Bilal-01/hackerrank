def beautifulDays(i, j, k):
    days = 0
    for x in range(i, j+1):
        reverse = (x%10)*10 + (x/10)
        if abs(x - reverse)%k == 0:
            days += 1

    return days

i = 20
j = 23
k = 6
print(beautifulDays(i, j, k))

"""
    19 => 91
    19%10 = 9
    19/10 = 1
    19%10 * 10 + 19/10 = 91
    
"""
def findDigits(n):
    digits = []
    tmp = n
    while tmp > 0:
        digits.append(tmp%10)
        tmp = int(tmp/10)
    
    count = 0
    for x in digits:
        if x == 0:
            continue
        if n%x == 0:
            count += 1
    
    return count


findDigits(9001)
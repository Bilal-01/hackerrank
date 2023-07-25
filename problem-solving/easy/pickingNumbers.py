def pickingNumbers(a):
    a.sort()
    arrmax = []
    for i in range(1, len(a)+1):
        maxLength = 1
        key = a[i-1]
        for j in range(i, len(a)):
            if(abs(a[j] - key) >=0 and abs(a[j]-key) <= 1):
                maxLength += 1
            if(j == len(a)-1) or (abs(a[j] - key) > 1):
                if maxLength > 0:
                    arrmax.append(maxLength)


    if len(arrmax) > 0:
        return max(arrmax)
    else:
        return 1




a = [0,0,0,0,0]
print(pickingNumbers(a))

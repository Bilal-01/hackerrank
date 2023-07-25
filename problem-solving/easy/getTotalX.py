# Between two sets

def getTotalX(a, b):
    first = a[-1]
    last = b[0]

    n = len(a)
    m = len(b)

    newList = a+b
    count = 0
    for i in range(first, last+1):
        flag = True
        for j in range(0, len(newList)):
            if(j < n and i%newList[j] != 0):
                flag = False
                break
            if(j >= n and newList[j]%i != 0):
                flag = False
                break

        if(flag):
            count = count + 1

    return count

if __name__ == "__main__":
    a = [2, 4]
    b = [16, 32, 96]
    print(getTotalX(a, b))
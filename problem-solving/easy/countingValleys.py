# Couting Valleys

def countingValleys(steps, path):
    valleys = 0
    accum = 0
    flag = False
    for i in range(0, steps):
        if(path[i] == 'U'):
            accum += 1
            if accum >= 0:
                flag = True
        if(path[i] == 'D'):
            accum -= 1
            if (accum < 0 and flag == True):
                valleys += 1
                flag = False

    return valleys

print(countingValleys(8, "UDDDUDUU"))



# Migratory Birds

def migratoryBirds(arr):
    freq = [0, 0, 0, 0, 0]

    for i in range(0, len(arr)):
        freq[arr[i] - 1] += 1

    max = 0
    maxInd = 0
    for i in range(0, len(freq)):
        if freq[i] > max:
            max = freq[i]
            maxInd = i

    return(maxInd+1)

arr = [1,1,2,2,3]
print(migratoryBirds(arr))
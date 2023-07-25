def hurdleRace(k, height):
    return max(max(height) - k, 0)

#test cases
height = [2, 5, 4, 5, 2]
k = 7

print(hurdleRace(k,height))
def jumpingOnClouds(c, k):
    energy = 100
    i=0
    n = len(c)
    while energy > 0:
        energy -= 1
        if c[(i+k)%n] == 1:
            energy -= 2
        if ( (i+k)%n ) == 0:
            break
        i += k

    return energy

c = [0, 0, 1, 0, 0, 1, 1, 0]
k = 2

print(jumpingOnClouds(c, k))
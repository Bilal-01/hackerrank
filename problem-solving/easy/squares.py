import math

def squares(a, b):
    countB = math.floor(math.sqrt(b))
    countA = math.floor(math.sqrt(a - 1))
    return countB - countA
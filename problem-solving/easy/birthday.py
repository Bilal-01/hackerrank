# Birthday

def birthday(s, d, m):
    ways = 0
    for i in range(0, len(s)-m+1):
        arrSum = sum(s[i:i+m])
        if(arrSum == d):
            ways = ways + 1

    return ways

if __name__ == "__main__":
    s = [4]
    d = 4
    m = 1
    print(birthday(s, d, m))
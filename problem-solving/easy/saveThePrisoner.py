def saveThePrisoner(n, m, s):
    last = (s + m - 1) % n
    if last == 0:
        last = n
    return last
    
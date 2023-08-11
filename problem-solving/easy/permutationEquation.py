def permutationEquation(p):
    y = []
    for x in range(1, len(p)+1):
        y.append(p.index(p.index(x)+1)+1)
    return y
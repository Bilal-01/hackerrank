def angryProfessor(k, a):
    tmp = [ i for i in a if i<= 0]

    if (k > len(tmp)):
        return "YES"
    else:
        return "NO"


k = 3
a = [-2, -1, 0, 1, 2]
angryProfessor(k, a)
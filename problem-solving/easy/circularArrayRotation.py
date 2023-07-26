def circularArrayRotation(a, k, queries):
    for i in range(0, k):
        x = a.pop()
        a.insert(0, x)

    for i in queries:
        print(a[i])

k = 2
q = [0,1,2]
a = [1,2,3]

circularArrayRotation(a, k, q)
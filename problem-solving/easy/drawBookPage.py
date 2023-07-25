# Drawing Book page
import math

def pageCount(n, p):
        front = 0
        back = 0

        if ((p==n) or (p==1)):
            return 0

        front = int(p/2)
        back = int(math.ceil((n-p)/2))

        return min(front, back)

print(pageCount(8, 5))

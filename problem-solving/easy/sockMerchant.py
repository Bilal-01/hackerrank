# Sales by match

import math

def sockMerchant(n, ar):
    ar.sort()
    pairs = 0
    j = 0
    for i in range(0, n-1):
        if j == (n-1):
            break
        if ar[j] == ar[j+1]:
            pairs += 1
            j += 2
            if j >= n:
                break
            continue
        j += 1

    return pairs

ar = [1,2,1,2,1,3]
print(sockMerchant(6, ar))
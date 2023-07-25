# Divisible Sum Pairs

def divisibleSumPairs(n, k, ar):
    count = 0
    for i in range(0, n):
        for j in range(i+1, n):
            sum = ar[i] + ar[j]
            if (sum % k == 0):
                count += 1

    return count

if __name__ == "__main__":
    ar = [1, 3, 2, 6, 1, 2]
    k=3
    print(divisibleSumPairs(len(ar), k, ar))

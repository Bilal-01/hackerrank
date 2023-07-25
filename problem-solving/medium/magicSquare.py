# Magic Square

"""
    TIP: 
        There are only 8 possible magic squares in 3x3 matrix, so you can hard code them.
        And compare all 8 with your input matrix. 
"""

def cost(a1, a2):
    cost = 0
    for i in range(0, 3):
        for j in range(0, 3):
            cost += abs((a1[i][j] - a2[i][j]))

    return cost

def formingMagicSquare(s):

    possibleSquares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    min_cost = 999

    for i in possibleSquares:
        if (cost(s, i) < min_cost):
            min_cost = cost(s, i)


    return min_cost


s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]
print(formingMagicSquare(s))
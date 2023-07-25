def binarySearch(array, x, low, high):

    if high >= low:
        mid = low + (high - low)//2

        if array[mid] <= x:
            if array[mid] == x:
              return mid
            else:
              tmp = binarySearch(array, x, low, mid-1)
              if tmp == -1:
                return mid
              else:
                return tmp

        # Search the left half
        elif array[mid] < x:
            return binarySearch(array, x, low, mid-1)

        # Search the right half
        else:
            return binarySearch(array, x, mid + 1, high)

    else:
        return -1

def climbingLeaderboard(ranked, player):
    newRankings = []
    ranks = []
    for i in range(0, len(ranked) - 1):
      if (ranked[i] != ranked[i+1]):
        ranks.append(ranked[i])

    if (len(ranked) > 1):
      if (ranked[-1] != ranked[-2]):
          ranks.append(ranked[-1])

    for i in range(0, len(player)):
      x = binarySearch(ranks, player[i], 0, len(ranks)-1)
      if x == -1:
        x = len(ranks)
      newRankings.append(x+1)

    print(ranks)

    return newRankings


if __name__ == "__main__":
    ranked = [1]
    player = [1, 1]
    newRankings = climbingLeaderboard(ranked, player)

    print(newRankings)
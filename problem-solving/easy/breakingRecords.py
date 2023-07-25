# Breaking records

def breakingRecords(score):
    max = 0
    min = 0

    maxScore = score[0]
    minScore = score[0]

    for i in range(1, len(score)):
        if score[i] < minScore:
            min = min + 1
            minScore = score[i]

        if score[i] > maxScore:
            max = max + 1
            maxScore = score[i]

    return [max, min]


if __name__ == "__main__":
    score = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    print(breakingRecords(score))

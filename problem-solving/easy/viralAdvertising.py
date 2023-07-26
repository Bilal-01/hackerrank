def viralAdvertising(n):
    cumLikes = 0
    shared = 5
    for i in range(0, n):
        cumLikes += int(shared/2) 
        shared = int(shared/2)*3

    return cumLikes

viralAdvertising(5) 
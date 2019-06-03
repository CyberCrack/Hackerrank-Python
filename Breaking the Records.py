def breakingRecords(scores):
    max, min = scores[0], scores[0]
    max_b, min_b = 0, 0
    for i in range(1, len(scores)):
        if (scores[i] > max):
            max_b += 1
            max = scores[i]
        if (scores[i] < min):
            min_b += 1
            min = scores[i]
    r = [max_b, min_b]
    return r


import math


def viralAdvertising(n):
    cummulative = 0
    ppl = 5
    if n == 1:
        return 2
    for i in range(n-1):
        liked = math.floor(ppl/2)
        cummulative += liked
        ppl += liked
    if not n % 2 == 0:
        ppl -= 1
    return ppl


print(viralAdvertising(3))

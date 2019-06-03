def permutationEquation(p):
    res = []
    p = [0] + p
    for i in range(1, len(p)):

        index1 = p.index(i)
        index2 = p.index(index1)
        if p[p[index2]] == i:
            res.append(index2)

    return res

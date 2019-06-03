import copy


def formingMagicSquare(s):
    cost = [100, 100, 100, 100, 100, 100, 100, 100]
    counter = 0
    matrix = [[4, 9, 2],
              [3, 5, 7],
              [8, 1, 6]]
    mirror_matrix = [[2, 9, 4],
                     [7, 5, 3],
                     [6, 1, 8]]
    if s == matrix:
        return 0
    else:

        for i in range(90, 360, 90):
            cmp_matrix = rotate(matrix, i)
            cmp_mirror_matrix = rotate(mirror_matrix, i)
            if s == cmp_matrix or s == cmp_mirror_matrix:
                return 0

        for k in range(0, 360, 90):
            cmp_matrix = rotate(matrix, k)
            cmp_mirror_matrix = rotate(mirror_matrix, k)
            copy_of_s = copy.deepcopy(s)
            inverse_copy_of_s = copy.deepcopy(s)

            for i in range(0, 3):
                for j in range(0, 3):
                    if copy_of_s[i][j] != cmp_matrix[i][j]:
                        cost[counter] = cost[counter] + abs(copy_of_s[i][j] - cmp_matrix[i][j])
                        copy_of_s[i][j] = cmp_matrix[i][j]
                    if inverse_copy_of_s[i][j] != cmp_mirror_matrix[i][j]:
                        cost[counter + 4] = cost[counter + 4] + abs(inverse_copy_of_s[i][j] - cmp_mirror_matrix[i][j])
                        inverse_copy_of_s[i][j] = cmp_mirror_matrix[i][j]

            counter += 1

        print(cost)
        return min(cost) - 100


def rotate(matrix, degree):
    if abs(degree) not in [0, 90, 180, 270, 360]:
        return
    if degree == 0:
        return matrix
    else:
        return rotate([list(item) for item in zip(*matrix[::-1])], degree - 90)


input_matrix = [[4, 5, 8], [2, 4, 1], [1, 9, 7]]
print(formingMagicSquare(input_matrix))

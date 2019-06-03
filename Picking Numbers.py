def pickingNumbers(a):
    array = sorted(a)
    max_length = 0
    length = 0
    unique_list = list(set(array))
    if len(unique_list) == 1:
        return len(a)

    count_of_each = []
    for i in unique_list:
        count_of_each.append(array.count(i))

    for i in range(0, len(unique_list) - 1):
        if unique_list[i + 1] - unique_list[i] <= 1:
            length = count_of_each[i] + count_of_each[i + 1]
        if length > max_length:
            max_length = length

    print(unique_list)
    print(count_of_each)
    return max_length


arr = [4, 6, 5, 3, 3, 1]
print(pickingNumbers(arr))

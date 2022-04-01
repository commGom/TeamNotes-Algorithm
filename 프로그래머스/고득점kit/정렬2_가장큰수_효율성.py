def solution(numbers):
    l = []
    for num in numbers:
        original = str(num)
        num = list(str(num))
        i = 0
        while len(num) <= 4:
            num.append(original[i])
            i = (i + 1) % len(original)
        num = int("".join(num))
        l.append([num, original])

    # ex1. [6, 10, 2]
    # l = [[66666, '6'], [10101, '10'], [22222, '2']]
    # ex2. [3, 30, 34, 5, 9]
    # l = [[33333, '3'], [30303, '30'], [34343, '34'], [55555, '5'], [99999, '9']]

    l = sorted(l, reverse=True)
    return str(int("".join([item[1] for item in l])))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))

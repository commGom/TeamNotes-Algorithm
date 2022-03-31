def solution(array, commands):
    answer = []
    # command i,j,k
    # 1. i번째부터~j번째까지 자르고,
    # 2. 정렬 후
    # 3. k번째 수 answer에 추가
    for command in commands:
        i, j, k = command
        # 1
        temp = array[i-1:j]
        # 2
        temp.sort()
        # 3
        answer.append(temp[k-1])
    return answer


print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 0 0 1 1 2 2 3 4 5 5 6 7 8 9 9


def coefficient_sort(array):
    # 모든 범위를 포함하는 리스트 선언, 0으로 초기화, 배열안에 든 값 중 최대값 까지 idx에 담을 것이다. 그리고 idx가 숫자가 되며 카운트한 값이 원소값으로 들어간다.
    values = [0]*(max(array)+1)

    # 배열을 돌면서 해당하는 값=idx에 count값 +1을 더해준다.
    for i in range(len(array)):
        values[array[i]] += 1

    # 리스트에 정렬 정보까지 for문 돌면서 해당하는 idx(실제배열에 들어있던 값) 개수만큼 출력
    for i in range(len(values)):
        for j in range(values[i]):
            print(i, end=" ")


coefficient_sort(array)

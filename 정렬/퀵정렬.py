array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    # pivot을 첫번째 원소로 잡는다
    pivot = start
    # 왼쪽은 pivot 다음 부터 순차적으로 진행, 오른쪽은 끝 값부터 진행
    left = start+1
    right = end
    # left의 값이 right 값보다 작다면, 계속 진행,
    while(left <= right):
        # 피벗보다 큰 데이터를 찾을 때까지 (왼쪽과 pivot)
        while(left <= end and array[left] <= array[pivot]):
            # 왼쪽 기준이 끝 idx보다 작고, 왼쪽 idx의 값이 pivot에 있는 값보다 작으면 왼쪽을 한 칸 +1
            left += 1
        # 피벗보다 작은 데이터를 찾을 때 까지 (오른쪽과 pivot)
        while(right > start and array[right] >= array[pivot]):
            # 오른쪽 idx 값이 시작 idx 보다 크고, 오른쪽 idx에 있는 원소값이 pivot에 있는 원소 값보다 크면 오른쪽을 -1
            right -= 1
        if(left > right):
            # 왼쪽기준과 오른쪽기준이 크로스가 난다면, pivot과 작은 데이터를 교체 => 이렇게 하면 pivot과 작은데이터(right 크로스가 일어나서)를 바꿔주니까 pivot을 기준으로 왼쪽은 pivot보다 작은 값, 오른쪽은 pivot 보다 큰값이 된다.
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[left], array[right] = array[right], array[left]

    # 분할이 다 된 다음 quick_sort() 함수를 재귀 호출->왼쪽, 오른쪽
    quick_sort(array, start, right-1)
    quick_sort(array, right+1, end)


quick_sort(array, 0, len(array)-1)
print(array)

array2 = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort_using_python(array):
    # 리스트가 하나의 원소만 담고 있으면 종료
    if len(array) <= 1:
        return array
    # pivot을 첫번째 원소로
    pivot = array[0]
    # pivot을 뺀 나머지 원소로 이루어진 함수 정의 tail
    tail = array[1:]

    # 분할된 왼쪽 부분 pivot에 있는 원소값 보다 작은 값을 가진 원소들->왼쪽으로
    left_side = [x for x in tail if x <= pivot]
    # 분할된 오른쪽 부분 pivot에 있는 원소값 보다 큰 값을 가진 원소들 ->오른쪽으로 넣기
    right_side = [x for x in tail if x > pivot]

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 재귀호출해주고 가운데는 pivot 넣고 전체 리스트 반환
    return quick_sort_using_python(left_side)+[pivot]+quick_sort_using_python(right_side)


print(quick_sort_using_python(array2))

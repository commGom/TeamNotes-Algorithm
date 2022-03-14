# 정렬 

## : 데이터를 특정 기준에 따라 순서대로 나열하는 것
## : 상황에 따라서 적절한 정렬 알고리즘 이용
## : 오름차순 기준으로 구현해 볼 것이다.

## 선택 정렬 알고리즘 (Selection Sorting) -> O(N^2)
### : 처리되지 않은 데이터 중에서 가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸는 것 반복

```python

def selection_sort(data):
    for i in range(len(data)):
        min_idx = i  # 가장 작은 원소 값을 찾아서 index를 변수 지정하여 i 위치에 있는 값과 원소값 바꾸기
        for j in range(i+1, len(data)):
            if data[min_idx] > data[j]:  # min_idx에 최소값을 찾기 위해 작은 값이 나오면 바꿔주기 위한 조건문
                min_idx = j  # 인덱스 j에 있는 원소값이 작으면

        data[i], data[min_idx] = data[min_idx], data[i]  # 값 change

```

## 삽입 정렬 알고리즘 (Insertion Sorting) 
### : 처리되지 않은 데이터를 하나씩 골라 적절한 위치에 삽입 

```python

def insertion_sort(data):
    for i in range(1, len(data)):
        for j in range(i, 0, -1):
            if data[j-1] > data[j]:
                data[j], data[j-1] = data[j-1], data[j]
            else:  # 작거나 같을 경우 앞에 부분은 다 정렬과정을 거쳐서 왔다.
                break


```

## 퀵 정렬 알고리즘 (Quick Sorting) -> 평균적으로 : O(NlogN), pivot 값 설정에 따라 최악의 경우 N^2
### : 기준 데이터(pivot)를 설정하고 그 기준보다 큰 데이터와 작은 데이터의 위치를 바꾸는 방법
### : pivot을 기준으로 왼쪽은 큰 값 오른쪽은 작은 값, 재귀적으로 호출해서 진행

- 기본 로직 그대로 구현
- 파이썬 문법 이용 (인덱스 슬라이싱, 리스트 컴프리헨션 이용)

```python

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

```

## 계수 정렬 -> O(N+K) : 데이터 개수 N, 데이터 중 최댓값이 K일 때
### : 특정 조건이 부합할 때만 사용할 수 있지만 매우 빠르게 동작한다.
### : 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때 사용 
### : 공간복잡도는 크지만, 시간복잡도는 작다 (데이터가 터무니 없이 클 경우 비효율적, 같은 값이 많을 경우 효율적이다.)

## 버블 정렬 -> 앞 뒤 비교 크면 바꿈. (모든 아이템 비교 ) O(N^2)
### : 좋은 알고리즘은 아니지만 이해하기 쉽다.
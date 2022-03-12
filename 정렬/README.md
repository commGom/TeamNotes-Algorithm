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

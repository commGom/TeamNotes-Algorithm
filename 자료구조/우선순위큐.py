import sys
import heapq

# 이터러블 객체를 받아서 정렬하는 함수 정의


def heapsort(iterable):
    # 우선순위 큐를 이용해서 담을 리스트 h
    h = []
    # 꺼낼 때, 정렬된 값으로 (작은 값 부터 나옴) 오름차순 값 담을 리스트 result
    result = []
    # 함수를 통해 들어오는 값의 모든 원소를 차례로 힙 자료구조에 넣는다
    for value in iterable:
        heapq.heappush(h, value)

    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for _ in range(len(h)):
        result.append(heapq.heappop(h))
    return result


n = int(input())
arr = []

# 임의의 값들을 입력받기
for i in range(n):
    arr.append(int(input()))

# 정의한 함수 호출
res = heapsort(arr)

for i in range(n):
    print(res[i])

# TeamNotes-Algorithm

## 시간 측정 

```python

import time

start = time.time()
# 로직 구현
end = time.time()
print(end-start)

```

## 반복문 for문 거꾸로

```python
    arr=[]
    for i in range(len(arr)-1, -1, -1):
        print(i)
```

## 입력

- 문자열로 받은 문자 한자리씩 리스트로 저장

```python

    characters = list(map(str, characters))

```

- 문자열로 받은 숫자 한자리씩 리스트로 저장, 2차원 배열로 저장

```python
import sys
input = sys.stdin.readline

number_list = list(map(int, input().rstrip()))

print(number_list)

# 입력값 : 02987
# 출력값 : [0,2,9,8,7]

number_list=[]
n,m=map(int,input().rstrip().split())
for _ in range(n):
    number_list.append(list(map(int, input().rstrip())))

# 입력값 : 4 5
# 00110
# 00011
# 11111
# 00000
# 출력값 : [[0,0,1,1,0],[0,0,0,1,1],[1,1,1,1,1],[0,0,0,0,0]]
```

- 띄어 쓰기로 숫자 입력 받아서 리스트로 정렬된 상태로 저장

```python

import sys
input = sys.stdin.readline

input_sorted_list=sorted(list(map(int, input().rstrip().split())), reverse=True)


# 입력값 : # 2 3 1 2 2
# 출력값 : [3,2,2,2,1]

```

## 해쉬(Hash), 딕셔너리 (매핑형 자료 구조)

- dic=dict() or dic={}을 이용하여 정의
- key:value 쌍으로 구성
- 인덱싱을 대신하여 ["key"]값으로 접근
- dic[key]=value로 값 설정 가능 (단일 수정)
- dic.update({key:value}) : 키가 없는 값이면 추가, 키가 있는 값이면 변경 (다중 수정)
- del dic[key] : 딕셔너리에서 해당 key값을 가지는 key,value 쌍 삭제
- dic.keys() : 키 값들을 리스트로 받는다
- dic.values() : value 값들을 리스트로 받는다
- dic.items() : (key,value) 튜플로 구성된 값들을 리스트로 받는다
- dic.get(key) : 해당 하는 key대한 value를 가져옴, dic.get(key,key)하면 없을 경우 key값을 그대로
- dic.copy() or copy(dic) : 딕셔너리 복사
- 'key' in dic : dictionary 안에 해당 키값을 가지고 있는지 확인 (필요시 for문 이용하면서 if 조건문 사용하면 될 듯)
- https://blockdmask.tistory.com/566 => dictionary 정렬

```python
    dic=dict()  #dic={}
    for key, val in dic:
        print("key={key}, value={value}".format(key=key,value=val))

    for key in dic: # for key in dic.keys()
        print(f"key={key}") # f string 이용
        print("value={value}".format(value=dic[key]))  # string format 이용 

    for val in dic.values():
        print(f"value={value}")
    
```

## 재귀함수 (Recursive Function) : 자기자신을 다시 호출하는 함수

- recursion limit 설정

```python

import sys
sys.setrecursionlimit(10000)

```

- 호출하면 stack과 같은 형태로 함수가 메모리에 차례대로 쌓여서 동작
- 컴퓨터 메모리 한정된 크기만큼 자원을 가지고 있기 때문에 함수가 종료되지 않고 쌓이면서 호출만 하게 된다면 빠르게 메모리 과부하 재귀 기피 제한 설정
- while이나 for 문 없이 내용을 반복적으로 수행 가능, 재귀함수의 종료 조건 명시 필요(프로그램이 정해진 값을 반환할 수 있도록 설정)

- 무한루프 재귀함수

```python

def recursive_function():
    print('재귀함수 호출')
    recursive_function()


recursive_function()

```

- 종료조건 명시 재귀함수

```python

def recursive_function(i):
    # 종료 조건 명시 : i가 100일 경우 종료
    if i == 100:
        return
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수 호출하는 중')
    recursive_function(i+1)


recursive_function(1)

```

### 재귀함수 특징

- 복잡한 알고리즘을 간결하게 작성 가능
- 재귀함수는 반복문으로 동일한 기능 구현 가능
- 스택 라이브러리 대신 재귀 함수 이용하는 경우가 있다.

| 분류       | 제목              | 날짜 | 비고 |
| -------- | ----------------- | ------ |-----------------|
| 재귀함수   | 팩토리얼 구현        | 22-03-10      |반복적으로 구현, 재귀적으로 구현|
| 재귀함수   | 팩토리얼 구현        | 22-03-10      |반복적으로 구현, 재귀적으로 구현|

## 순열조합

### 순열 permutation

```python

import itertools

arr = ['A', 'B', 'C']
r=2
list_nPr = itertools.permutations(arr, r)

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

```

### 조합 combination

```python

import itertools

arr = ['A', 'B', 'C']
r=2
nCr = itertools.combinations(arr, r)
print(list(nCr))

# 결과 : [('A', 'B'), ('A', 'C'), ('B', 'C')]

```

## 백준

### 그리디

| 분류       | 제목              | 날짜 | 비고 |
| -------- | ----------------- | ------ |-----------------|
| 그리디   | 곱하기 혹은 더하기        | 22-03-08      ||
| 그리디   | 1이 될 때 까지         | 22-03-08      ||
| 그리디   | 모험가 길드        | 22-03-08      ||
| 그리디(백준)   | 11047 동전        | 22-03-08      ||

### 구현
| 분류       | 제목              | 날짜 | 비고 |
| -------- | ----------------- | ------ |-----------------|
| 구현   | 상하좌우        | 22-03-09      |f string|
| 구현   | 왕실의 나이트        | 22-03-09      |아스키코드<->문자|
| 구현   | 시각        | 22-03-09      |문자열 더하기 연산, 문자 포함하는지 조건문|
| 구현   | 문자열재정렬        | 22-03-09      |배열을 문자열로 변환, 문자<->숫자|

- 문자열 출력 f string 이용

```python

position = [0, 0]
print(f'위치는 {position[1]+1} {position[0]+1}')

```

- 아스키코드, 나이트 이동(8가지 경우)

```python

# ord('문자')->아스키 코드 chr('아스키코드')->문자
x = ord('소문자 알파벳')-ord('a')

# 나이트 L자 이동 (경우의 수 8가지)
# (1,2) (1,-2) (-1,2) (-1,-2) (2,1) (2,-1) (-2,1) (-2,-1)
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]

```

- 문자열 더하기 연산, 문자 포함하는지 조건문

```python

if '3' in str(h)+str(m)+str(s):
    answer += 1

```

- 문자<->숫자 str(숫자)->'숫자'문자열로 변환, int('숫자')->숫자로 변환
- 배열을 문자열로 변환 ''.join(배열)

```python

int(val)
answer = ''.join(answer_alpha)+str(answer_digit)

```

### 자료구조

| 분류       | 제목              | 날짜 | 비고 |
| -------- | ----------------- | ------ |-----------------|
| 자료구조   | stack        | 22-03-10      |리스트 뒷 idx 원소부터 출력|
| 자료구조   | queue        | 22-03-10      |from collections import deque|
| 자료구조   | 우선순위큐        | 22-03-11      |import heapq|
| 자료구조   | 트리순회        | 22-03-11      |전위, 중위, 후위 순회|

- 리스트 뒷 idx 원소부터 출력

```python

stack = []

# 삽입(5) -> 삽입 (2) -> 삽입(3) -> 삭제() -> 삽입(1) -> 삽입(4) -> 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack[::-1])  # 끝 idx 원소부터 출력 [1,2,5]
print(stack)  # idx : 0 원소부터 출력 [5,2,1]

```

- 힙자료구조에 값 넣고 빼기 (파이썬은 MIN heap)

```python

import heapq

# iterable은 임의의 갑들을 가진 자료형, h는 힙자료구조를 정의할 배열

# 함수를 통해 들어오는 값의 모든 원소를 차례로 힙 자료구조에 넣는다
for value in iterable:
    heapq.heappush(h, value)

# 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
for _ in range(len(h)):
    result.append(heapq.heappop(h))

```

### 정렬

| 분류       | 제목              | 날짜 | 비고 |
| -------- | ----------------- | ------ |-----------------|
| 정렬   |    선택정렬     | 22-03-12      |O(N^2) 시간복잡도, 배열 값 스와프|
| 정렬   |    삽입정렬     | 22-03-12      |O(N^2) 시간복잡도, 선택정렬보다 조금 효율적일 수 있다(정렬되어있을 수록)|
| 정렬   |    퀵정렬     | 22-03-13      |O(NlogN) 정렬된 데이터일 수록 비효율적, python 인덱스 슬라이싱, 리스트 컴프리헨션 이용|
| 정렬   |    계수정렬     | 22-03-13      |O(N+K) 같은 원소값이 많을 수록 효율적|
| 정렬   |    두배열의원소교체     | 22-03-13      ||
| 정렬   |    버블정렬     | 22-03-14      |O(N^2), 잘 안 쓰는 정렬 그냥 방법 단순|

- 배열 값 스와프

```python

array[i], array[j] = array[j], array[i]  # 값 change

```

### 그래프 탐색 알고리즘 (DFS, BFS)

| 분류       | 제목              | 날짜 | 비고 |
| -------- | ----------------- | ------ |-----------------|
| DFS   | dfs        | 22-03-10      |dfs 함수 정의, 재귀적으로 호출|
| BFS   | bfs        | 22-03-10      |bfs 함수 정의, queue 자료구조 이용|
| BFS   | 음료수 얼려먹기        | 22-03-10      |연결요소 찾기, connected component,bfs,dfs|
| BFS   | 미로탈출       | 22-03-10      |간선의 비용이 같을 때 최단거리 BFS|

- DFS 함수 정의

```python

# DFS 메서드 정의
# 각 노드 연결정보 표현하는 2차원 리스트 graph, 방문처리할 노드번호 v, 방문된 정보를 가진 1차원 리스트 visited
def dfs(graph, v, visited):
    # 1. 현재 노드 방문 처리 visited 리스트에 해당 노드번호에 해당하는 방 True(방문표시)
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 graph[v] 에는 인접한 노드 정보가 들어있음
    for i in graph[v]:
        # 방문하지 않은 노드가 있으면 재귀적으로 호출하여 방문처리 해준다
        if not visited[i]:
            dfs(graph, i, visited)

```

- BFS 함수 정의

```python

from collections import deque

# 간선 연결 정보를 이차원 배열에 넣음 graph, 시작 노드 번호 start, 방문 노드 정보 일차원 배열 visited
def bfs(graph, start, visited):
    # 1. queue 자료구조에 방문 노드 정보 넣기
    queue = deque([start])

    # queue가 빌 때까지 무한 반복
    while queue:
        # 2. 큐에서 하나의 원소(방문노드번호) 뽑기
        v = queue.popleft()

        # 3. 현재 노드 방문처리
        visited[v] = True
        print(v, end=" ")

        # 4. 현재 방문한 노드에 연결된 다른 노드들 queue에 담기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)

```

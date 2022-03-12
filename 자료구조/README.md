# 자료구조

## Stack : 선입후출

### : Python에서는 list 자료구조 이용 [] or list() 정의하고 삽입: append(값)과 삭제: pop() 연산

### : Java new Stack<>() push(값) pop(), 제일 처음 들어간 데이터 꺼내기 peek()

## Queue : 선입선출

### : python collections import deque 라이브러리 이용 삽입: append(값)과 삭제: leftpop() 연산 이용

### : Java new LinkedList<>() 삽입 : offer(값), 삭제 : poll()

## 우선순위 큐 (Priority Queue) : 우선순위가 가장 높은 데이터를 가장 먼저 삭제하는 자료구조

### : 리스트를 이용하여 구현 (삽입 : O(1), 삭제 : O(N))

### : 힙(Heap)을 이용하여 구현 (삽입 : O(logN), 삭제 : O(logN)) 

- python heapq 라이브러리 이용 (최소힙) heapq.heappush(리스트,값), heapq.heappop(값)
- python heapq max 힙을 이용하고 싶을 때, 값에 -1를 음수를 만들어 넣고 음수로 꺼내면 된다.

## 트리 : 계층적인 구조를 표현할 때 사용할 수 있는 자료구조

### 트리 순회 : 트리자료구조에 포함되어있는 모든 원소 확인할 때 사용 (전위 중위 후위)

- 전위 순회(Preorder Traversal) : 루트->왼쪽자식->오른쪽자식 노드 순으로 
- 중위 순회(Inorder Traversal) : 왼쪽자식->루트->오른쪽자식 노드 순으로
- 후위 순회(Postorder Traversal) : 오른쪽자식->루트->왼쪽자식 노드 순으로
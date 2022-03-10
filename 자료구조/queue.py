from collections import deque

queue = deque()

# 삽입(5) -> 삽입 (2) -> 삽입(3) -> 삭제() -> 삽입(1) -> 삽입(4) -> 삭제()
queue.append(5)
queue.append(2)
queue.append(3)
queue.pop()
queue.append(1)
queue.append(4)
queue.pop()

print(queue)  # 5,2,1

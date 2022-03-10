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

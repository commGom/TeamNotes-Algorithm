import itertools

# 1. zip()

# 동일한 개수로 이루어진 iterable한 객체들을 인수로 받아 묶어서 iterator로 반환
z = zip([1, 2, 3], ('A', 'B', 'C'))
print(next(z))  # (1, 'A')
print(next(z))  # (2, 'B')
print(next(z))  # (3, 'C')

# 2. all()

# iterable한 객체를 인수로 받아서 원소가 모두 참이면 True, 아니면 False를 반환
a = all([1, 2, 3])  # True
a = all([0, 1, 2])  # False

# 3. any()

# iterable한 객체를 인수로 받아서 원소가 하나라도 참이면 True, 아니면 False를 반환
a = any([0, 1, 2])  # True
a = any([0, False, []])  # False

# 4. chain()

# iterable한 객체들을 인수로 받아 하나의 iterator로 반환
c1 = [1, 2]
ca = ['A', 'B']
c = itertools.chain(c1, ca)
print(next(c))  # 1
print(next(c))  # 2
print(next(c))  # A
print(next(c))  # B

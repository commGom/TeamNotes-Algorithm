import sys
from tabnanny import check
input = sys.stdin.readline

# 모험가의 수 N
N = int(input().rstrip())

# 각 모험가의 공포도를 list에 담아서 오름차순 정렬
adventurers = sorted(list(map(int, input().rstrip().split())))

# 입력값 확인
# print(N, adventurers)

answer = 0
# 모험가 수
count = 0
for extent in adventurers:
    count += 1
    if count >= extent:
        answer += 1
        count = 0

print(answer)


# 5
# 2 3 1 2 2

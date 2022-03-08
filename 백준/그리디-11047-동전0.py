import sys
input = sys.stdin.readline

# 동전 개수의 최솟값 답
answer = 0

# 동전 종류 개수 N, 동전 가치의 합(잔돈) K
N, K = map(int, input().split())

coins = []
# 1. 동전 종류 개수 N 만큼 동전 종류 값 받아서 리스트에 넣기
for _ in range(N):
    coins.append(int(input().rstrip()))
# 입력 값 확인
# print(N,K,coins)

# 2. 큰 돈 부터 넣기
coins.reverse()
for coin in coins:
    if K == 0:
        break
    if K >= coin:
        count = K//coin
        K -= count*coin
        answer += count
print(answer)

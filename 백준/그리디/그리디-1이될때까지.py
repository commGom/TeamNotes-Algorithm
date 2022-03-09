import sys
input = sys.stdin.readline

# 주어진 숫자 N, 나눌 수 있는 값 K
N, K = map(int, input().rstrip().split())

answer = 0
while True:
    # K로 나눠질 때 까지의 값 찾기, 그 전까진 1로 빼야하니까
    dividable_num = (N//K)*K
    answer += N-dividable_num
    # print(N, dividable_num, answer)

    # K로 나누는 횟수 1번 더해주기
    N //= K
    answer += 1

    if N < K:
        break

answer += N-1
print(answer)

# 17 4 -> 3
# 25 5 -> 2
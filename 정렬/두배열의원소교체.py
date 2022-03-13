import sys
input = sys.stdin.readline
# 입력값
# 5 3
# 1 2 5 4 3
# 5 5 6 6 5
# 출력값 26

# 두 배열 각각 원소의 개수 N, 바꿀 수 있는 횟수 K
N, K = map(int, input().rstrip().split())
print(N, K)
# 두 배열 A(오름차순), B(내림차순)

arr_A = list(map(int, input().rstrip().split()))
arr_A.sort()
arr_B = list(map(int, input().rstrip().split()))
arr_B.sort(reverse=True)
# print(arr_A, arr_B)
for _ in range(K):
    if arr_A[0] < arr_B[0]:
        tmp = arr_A[0]
        arr_A[0] = arr_B[0]
        arr_B[0] = tmp
        arr_A.sort()
        arr_B.sort(reverse=True)
        # print(arr_A, arr_B)
    else:
        break

print(sum(arr_A))

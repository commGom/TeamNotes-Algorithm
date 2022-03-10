import sys
input = sys.stdin.readline

number_list = list(map(int, input().rstrip()))

# 첫 번째 수로 시작하기
answer = number_list[0]

for i in range(1, len(number_list)):
    result = answer*number_list[i]
    if result == 0 or result == answer:
        answer += number_list[i]
    else:
        answer = result
print(answer)

# 02984 -> 576
# 567 -> 210
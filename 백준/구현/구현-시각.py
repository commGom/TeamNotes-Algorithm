import sys
input = sys.stdin.readline

# 0~23까지 시(hour) 중 숫자 하나 N
# H=5 ->
H = int(input().rstrip())
answer = 0
for h in range(H+1):
    for m in range(60):
        for s in range(60):
            # 매 시각안에 3을 포함하고 있다면 +1
            if '3' in str(h)+str(m)+str(s):
                answer += 1
print(answer)

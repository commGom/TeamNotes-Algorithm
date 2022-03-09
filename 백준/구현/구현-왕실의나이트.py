import sys
input = sys.stdin.readline

# input_value='a1'
input_value = input().rstrip()

# 위치 초기화 해놓기
x = ord(input_value[0])-ord('a')
y = int(input_value[1])-1

# 입력값으로 위치 좌표 확인
print(x, y)

# 나이트 L자 이동 (경우의 수 8가지)
# (1,2) (1,-2) (-1,2) (-1,-2) (2,1) (2,-1) (-2,1) (-2,-1)
dx = [1, 1, -1, -1, 2, 2, -2, -2]
dy = [2, -2, 2, -2, 1, -1, 1, -1]
# 움직일 수 있는 경우의 수
answer = 0
for i in range(len(dx)):
    nx = x+dx[i]
    ny = y+dy[i]

    if 0 <= nx < 8 and 0 <= ny < 8:
        answer += 1
print(answer)

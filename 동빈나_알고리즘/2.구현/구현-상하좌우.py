import sys
input = sys.stdin.readline
# 입력 값 받기, 공간의 크기 N, 움직인 방향 리스트
# N=5
N = int(input().rstrip())
# moves=['R','R','R','U','D']
moves = input().rstrip().split()
position = [0, 0]
# R : c-> +1,
# L : c-> -1,
# U : r-> -1,
# D : r-> +1
for move in moves:
    c = position[0]
    r = position[1]
    if move == 'R' and c < N-1:
        position[0] = c+1
    elif move == 'L' and c > 0:
        position[0] = c-1
    elif move == 'D' and r < N-1:
        position[1] = r+1
    elif move == 'U' and r > 0:
        position[1] = r-1
# 5
# R R R U D D
print(f'위치는 {position[1]+1} {position[0]+1}')
# 정답 3 4

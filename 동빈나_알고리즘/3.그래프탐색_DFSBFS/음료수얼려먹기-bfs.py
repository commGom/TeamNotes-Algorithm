from collections import deque
import sys
input = sys.stdin.readline

# bfs 정의 받은 위치에서 인접한 위치가 0을 가지면 queue 담기 frame[i][j] 1로 만들기
# 상하좌우 dx=[0,0,-1,1] dy=[-1,1,0,0]


def bfs(i, j, frame):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    queue = deque([(i, j)])
    while queue:
        # 2. 큐에서 꺼내서 0->1로 만들기
        x, y = queue.popleft()
        frame[x][y] = 1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < len(frame) and 0 <= ny < len(frame[0]):
                if frame[nx][ny] == 0:
                    queue.append((nx, ny))


frame = []
n, m = map(int, input().rstrip().split())
for _ in range(n):
    frame.append(list(map(int, input().rstrip())))

# 4 5
# 00110
# 00011
# 11111
# 00000
print(frame)


# 뚤려있는 부분이 0, 0으로 이루어진 만들 수 있는 얼음 개수
# 내가 생각한 로직 0인 부분을 만나면 answer count 1을 더하고 BFS로 인접한 0인 부분 다 1로 만들기
answer = 0
for i in range(n):
    for j in range(m):
        if frame[i][j] == 0:
            print(i, j)
            answer += 1
            print(frame)
            bfs(i, j, frame)

print(f'만들어지는 얼음 갯수 {answer}')

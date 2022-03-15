from collections import deque
import sys
input = sys.stdin.readline


frame = []
n, m = map(int, input().rstrip().split())
for _ in range(n):
    frame.append(list(map(int, input().rstrip())))

# 괴물있는 부분 0, 괴물있는 부분 1
# 5 6
# 101010
# 111111
# 000001
# 111111
# 111111

print(frame)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if frame[nx][ny] == 0:
                    continue
                if frame[nx][ny] == 1:
                    frame[nx][ny] = frame[x][y]+1
                    queue.append((nx, ny))
    return frame[n-1][m-1]

print(bfs(0, 0))

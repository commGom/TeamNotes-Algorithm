from collections import deque

# 간선 연결 정보를 이차원 배열에 넣음 graph, 시작 노드 번호 start, 방문 노드 정보 일차원 배열 visited


def bfs(graph, start, visited):
    # 1. queue 자료구조에 방문 노드 정보 넣기
    queue = deque([start])

    # queue가 빌 때까지 무한 반복
    while queue:
        # 2. 큐에서 하나의 원소(방문노드번호) 뽑기
        v = queue.popleft()

        # 3. 현재 노드 방문처리
        visited[v] = True
        print(v, end=" ")

        # 4. 현재 방문한 노드에 연결된 다른 노드들 queue에 담기
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문된 정보 담을 리스트
visited = [False]*len(graph)

# 정의된 DFS 함수 1번 노드부터 시작하여 호출
bfs(graph, 1, visited)

# 결과 1 2 3 8 7 4 5 6

# DFS 메서드 정의
# 각 노드 연결정보 표현하는 2차원 리스트 graph, 방문처리할 노드번호 v, 방문된 정보를 가진 1차원 리스트 visited
def dfs(graph, v, visited):
    # 1. 현재 노드 방문 처리 visited 리스트에 해당 노드번호에 해당하는 방 True(방문표시)
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문 graph[v] 에는 인접한 노드 정보가 들어있음
    for i in graph[v]:
        # 방문하지 않은 노드가 있으면 재귀적으로 호출하여 방문처리 해준다
        if not visited[i]:
            dfs(graph, i, visited)


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
dfs(graph, 1, visited)

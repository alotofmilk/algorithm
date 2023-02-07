import sys
sys.setrecursionlimit(10**6)
N, M, R = map(int,sys.stdin.readline().split())
graph = [[] for i in range(N+1)]
visited = [0] * (N+1)
cnt = 1

def dfs(graph,start,visited):
    global cnt
    visited[start] = cnt
    for adj in graph[start]:
        if visited[adj] == 0:
            cnt += 1
            dfs(graph,adj,visited)

for i in range(M):
    u, v = map(int,sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(N+1):
    graph[i].sort()

dfs(graph,R,visited)

for i in range(1, N+1):
    print(visited[i])

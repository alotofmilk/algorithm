import sys
sys.setrecursionlimit(10000)

dX = [-1,1,0,0,1,1,-1,-1]
dY = [0,0,-1,1,1,-1,1,-1]

def dfs(x,y):
    visited[x][y] = True
    if graph[x][y] == 1:
        for i in range(8):
            nX = x + dX[i]
            nY = y + dY[i]
            if 0 <= nX < h and 0 <= nY < w:
                if graph[nX][nY] == 1 and visited[nX][nY] == False:
                    dfs(nX,nY)

while True:
    w, h = map(int,sys.stdin.readline().split())
    if w == 0 and h == 0: break
    else:
        graph = [list(map(int,sys.stdin.readline().split())) for i in range(h)]
        visited = [[False] * w for i in range(h)]; answer = 0
        for x in range(h):
            for y in range(w):
                if visited[x][y] == False and graph[x][y] == 1:
                    dfs(x,y)
                    answer += 1
                else: continue
    print(answer)
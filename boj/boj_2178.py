import sys
from collections import deque

dx = [1,-1,0,0]
dy = [0,0,1,-1]

n,m = map(int,sys.stdin.readline().split())
graph = []

for _ in range(n):
    lst = list(map(int,sys.stdin.readline().rstrip()))
    graph.append(lst)

visited = [[False]*(m) for _ in range(n)]


def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y]=True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]==1:
                if not visited[nx][ny]:
                    q.append([nx,ny])
                    visited[nx][ny]=True
                    graph[nx][ny] = graph[x][y] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j]==1 and visited[i][j]==False:
            bfs(i,j)

print(graph[-1][-1])





import sys
from collections import deque
graph = []

n,m =map(int,sys.stdin.readline().split())

for _ in range(n):
    lst = list(map(int,input()))
    graph.append(lst)

visited = [[False]*m for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    q = deque()
    q.append([x,y])
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
                    graph[nx][ny] = graph[x][y]+1
bfs(0,0)
print(graph[-1][-1])


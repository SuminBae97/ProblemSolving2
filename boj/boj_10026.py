import sys
from collections import deque
n = int(sys.stdin.readline())

graph = []
dx=[1,-1,0,0]
dy=[0,0,1,-1]

for _ in range(n):
    lst = list(sys.stdin.readline().rstrip())
    graph.append(lst)
visited = [[False]*n for _ in range(n)]

def bfs_none(x,y,color):
    q = deque()
    q.append([x,y])
    visited[x][y]=True

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<n and graph[nx][ny]==color:
                if not visited[nx][ny]:
                    visited[nx][ny]=True
                    q.append([nx,ny])




r_count= 0
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R' and not visited[i][j]:
            bfs_none(i,j,'R')
            r_count+=1


visited = [[False]*n for _ in range(n)]
b_count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]=='B' and not visited[i][j]:
            bfs_none(i,j,'B')
            b_count+=1



visited = [[False]*n for _ in range(n)]
g_count = 0

for i in range(n):
    for j in range(n):
        if graph[i][j]=='G' and not visited[i][j]:
            bfs_none(i,j,'G')
            g_count+=1


for i in range(n):
    for j in range(n):
        if graph[i][j]=='G':
            graph[i][j]='R'

visited = [[False]*n for _ in range(n)]
rg_count = 0
for i in range(n):
    for j in range(n):
        if graph[i][j]=='R' and not visited[i][j]:
            bfs_none(i,j,'R')
            rg_count+=1



print((r_count+g_count+b_count) ,rg_count+b_count )
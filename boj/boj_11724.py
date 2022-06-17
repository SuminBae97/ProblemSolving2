import sys
from collections import deque
#sys.setrecursionlimit(10**6)
n,m = map(int,sys.stdin.readline().split())

visited = [False]*(n+1)
graph =[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    q = deque([start])
    visited[start]=True
    while q:
        v = q.popleft()
        for val in graph[v]:
            if not visited[val]:
                visited[val]=True
                q.append(val)
count=0
for i in range(1,n+1):
    if not visited[i]:
        bfs(i)
        count+=1
print(count)

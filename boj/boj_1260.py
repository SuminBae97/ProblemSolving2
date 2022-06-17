import sys
from collections import deque

n,m,start = map(int,sys.stdin.readline().split())
sys.setrecursionlimit(10**6)
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)


for lst in graph:
    lst.sort()


def dfs(start):
    visited[start]=True
    print(start,end=' ')
    for val in graph[start]:
        if not visited[val]:
            dfs(val)

def bfs(start):
    q = deque([start])
    visited[start]=False
    while q:
        val = q.popleft()
        print(val,end=' ')
        for v in graph[val]:
            if visited[v]:
                visited[v]=False
                q.append(v)

dfs(start)
print()
bfs(start)

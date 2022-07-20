import sys
from collections import deque

n,m,start = map(int,sys.stdin.readline().split())

visited = [True]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for node in graph:
    node.sort()


def bfs(start):
    q = deque()
    q.append(start)
    visited[start]=True

    while q:
        val = q.popleft()
        print(val,end=' ')
        for nxt in graph[val]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt]=True

def dfs(start):
    print(start, end=' ')
    visited[start]=False
    for nxt in graph[start]:
        if visited[nxt]:
            dfs(nxt)


dfs(start)
print()
bfs(start)




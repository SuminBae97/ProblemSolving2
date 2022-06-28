import sys
from collections import deque
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*(n+1)

def bfs(x):
    q = deque()
    q.append(x)
    visited[x]=True
    while q:
        val = q.popleft()
        for nxt in graph[val]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt]=True

bfs(1)
print(visited.count(True)-1)



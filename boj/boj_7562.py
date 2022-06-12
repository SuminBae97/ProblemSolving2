import sys
from collections import deque
test_case = int(sys.stdin.readline())
dx = [-1, -2, -2, -1, 1, 2, 2, 1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]



def bfs(start_x,start_y,end_x,end_y):
    q = deque()
    graph[start_x][start_y]=1
    q.append([start_x, start_y])
    visited[start_x][start_y]=True

    while q:
        a,b = q.popleft()
        if a==end_x and b==end_y:
            return

        for i in range(8):
            x = a+dx[i]
            y = b+dy[i]

            if 0<=x<n and 0<=y<n:
                if not visited[x][y]:
                    visited[x][y] = True
                    q.append([x, y])
                    graph[x][y] = graph[a][b] + 1







for i in range(test_case):
    n = int(sys.stdin.readline())
    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    graph = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    bfs(start_x, start_y, end_x, end_y)
    print(graph[end_x][end_y] - 1)


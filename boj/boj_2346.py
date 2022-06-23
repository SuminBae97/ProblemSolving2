import sys
from collections import deque
n = int(input())
q = deque(enumerate(map(int, input().split())))
answer=[]

while q:
    k,v = q.popleft()
    answer.append(k+1)
    if v>0:
        q.rotate(-v+1)
    elif v<0:
        q.rotate(-v)
print(answer)


print(' '.join(map(str, answer)))
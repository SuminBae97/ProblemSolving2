import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque(enumerate(map(int,sys.stdin.readline().split())))
answer = []
while q:
    val,mov = q.popleft()
    answer.append(val+1)

    if mov>0:
        q.rotate(-mov+1)
    elif mov<0:
        q.rotate(-mov)

for v in answer:
    print(v,end=' ')


import sys
table = []
n = int(sys.stdin.readline())

for _ in range(n):
    lst = list(map(int,sys.stdin.readline().split()))
    table.append(lst)


for i in range(1,n):
    for j in range(3):
        if j==0:
            table[i][j] = min(table[i-1][1]+table[i][j],table[i-1][2]+table[i][j])
        elif j==1:
            table[i][j] = min(table[i-1][0]+table[i][j],table[i-1][2]+table[i][j])
        elif j==2:
            table[i][j] = min(table[i - 1][0] + table[i][j], table[i - 1][1] + table[i][j])

print(min(table[-1]))
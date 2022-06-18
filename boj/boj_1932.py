import sys
n= int(sys.stdin.readline())
tree =[]

for _ in range(n):
    lst = list(map(int,sys.stdin.readline().split()))
    tree.append(lst)

for i in range(1,n):
    for j in range(len(tree[i])):
        if j==0:
            tree[i][j] = tree[i-1][j] + tree[i][j]

        elif j==len(tree[i])-1:
            tree[i][j] = tree[i-1][j-1] + tree[i][j]

        else:
            tree[i][j] = max(tree[i-1][j-1] + tree[i][j] , tree[i-1][j]+tree[i][j])

print(max(tree[-1]))





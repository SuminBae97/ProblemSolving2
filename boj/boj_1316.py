import sys

n = int(input())
lst =[]
for i in range(n):
    lst.append(sys.stdin.readline().rstrip())

total=len(lst)
ct=0
for word in lst:
    for i in range(len(word)-1):
        if word[i]==word[i+1]:
            pass
        else:
            if word[i] in word[i+1:]:
                ct+=1
                break
print(total-ct)




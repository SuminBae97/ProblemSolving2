import sys
from collections import Counter

word = sys.stdin.readline().rstrip()
word = word.lower()

lst = []
for w in word:
    lst.append(w)

ct = Counter(word)
val = []
for v in ct.values():
    val.append(v)

max_val  = max(val)
ind = val.index(max_val)
val.remove(max_val)
if max_val in val:
    print("?")

else:
    print(ct.most_common()[0][0].upper())




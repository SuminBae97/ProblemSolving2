import sys
test_case = int(input())

for _ in range(test_case):
    a = sys.stdin.readline()
    answer = []
    for v in a:
        answer.append(v)

    count = 0
    for i in range(len(answer)):
        if i == 0 and answer[i] == 'O':
            count += 1
            continue

        if answer[i] == 'O':
            if answer[i - 1] != 'O':
                count += 1
                continue
            while answer[i] == 'O':
                if i < 0:
                    break
                count += 1
                i = i - 1
    print(count)







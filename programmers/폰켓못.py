from collections import Counter
def solution(nums):
    pick = len(nums) // 2
    ct = Counter(nums)
    answer = None
    if len(ct) > pick:
        answer = pick
    else:
        answer = len(ct)

    return answer

# print(solution([3,3,3,2,2,4]))
from collections import Counter


def solution(participant, completion):
    ct1 = Counter(participant)
    ct2 = Counter(completion)

    return ((ct1 - ct2).most_common()[0][0])

# participant = ["mislav", "stanko", "mislav", "ana"]
# completion = ["stanko", "ana", "mislav"]
#
# print(solution(participant,completion))
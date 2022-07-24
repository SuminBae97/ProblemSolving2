
def solution(phone_book):
    phone_book.sort()
    answer = True
    print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer= False
    return answer

print(solution(["12","123","1235","567","88"]))
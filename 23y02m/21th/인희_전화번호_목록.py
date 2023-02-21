def solution(phone_book):
    
    # 오름차순으로 정렬
    phone_book.sort()
    
    for i, j in zip(phone_book, phone_book[1:]):
        if j.startswith(i):
            return False
    return True
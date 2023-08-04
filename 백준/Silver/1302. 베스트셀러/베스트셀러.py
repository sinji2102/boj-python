import sys

input = sys.stdin.readline
test_case = int(input().rstrip())
book = []

for _ in range(test_case) :
    book.append(input().rstrip())

cnt = [1 for _ in range(test_case)]

book.sort()

for i in range(1, test_case) :
    if i == test_case :
        if book[i-1] == book[i] :
            cnt[i] = cnt[i] + 1
    
    if book[i-1] == book[i] :
        cnt[i] = cnt[i-1] + 1

print(book[cnt.index(max(cnt))])
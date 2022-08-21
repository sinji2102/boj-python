test_c = int(input())

list_ = []
list_ = list(map(int, input().split()))
v = int(input())
cnt = 0
for i in list_ :
    if v == i :
        cnt += 1
    
print(cnt)
    
    
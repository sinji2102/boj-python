import sys
input = sys.stdin.readline

test_c = int(input())

list_ = list(map(int, input().rstrip().split()))
cnt = 0

for i in list_ :
    not_cnt = 0

    if i > 1 :
        for j in range(2, i) :
            if i % j == 0 :
                not_cnt += 1
                break
        
        if not_cnt == 0 :
            cnt += 1

print(cnt)
        
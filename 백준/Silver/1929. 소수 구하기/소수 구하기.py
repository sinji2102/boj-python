import sys
input = sys.stdin.readline

start, finish = map(int, input().rstrip().split())

for i in range(start, finish + 1) :
    if i != 1 :
        for j in range(2, int(i**0.5) + 1) :   # 에라토스테네스의 체
            if i % j == 0 :
                break
        else :
            print(i)
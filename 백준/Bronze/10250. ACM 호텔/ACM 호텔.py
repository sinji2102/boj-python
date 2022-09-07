import sys
input = sys.stdin.readline

test_c = int(input())


for i in range(test_c) :
    H, W, N = map(int, input().rstrip().split())
    
    x = N % H
    y = N // H

    if x == 0 :
        print((H * 100) + y)
    else :
        print((x * 100) + y + 1)

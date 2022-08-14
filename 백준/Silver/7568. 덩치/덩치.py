import sys
input = sys.stdin.readline

test_c = int(input().strip())
people = []

for i in range(test_c) :
    x, y = map(int, input().strip().split())
    people.append((x, y))

for j in people :
    cnt = 1
    for n  in people :
        if j[0] < n[0] and j[1] < n[1] :
            cnt += 1
    print(cnt, end = " ")

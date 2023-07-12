import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    k = int(input())
    n = int(input())

    # 1부터 n까지 있는 리스트 생성
    cnts = [j for j in range(1, n+1)]

    for _ in range(k):
        for x in range(1, n):
            cnts[x] += cnts[x-1]

    print(cnts[-1])
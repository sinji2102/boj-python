import sys
input = sys.stdin.readline

while True :
    cnt = 0
    A = input().strip()
    if A == "#" :
        break

    A = A.upper()
    cnt += A.count("A")
    cnt += A.count("E")
    cnt += A.count("I")
    cnt += A.count("O")
    cnt += A.count("U")

    print(cnt)
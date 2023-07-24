import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case):
    list_ = list(input().split())

    print("Case #%i: " %(i+1), end="")
    for j in list_[::-1] :
        print(j,end=" ")
    if j != list_[0]:
        print("")
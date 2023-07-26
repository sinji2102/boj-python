import sys

input = sys.stdin.readline

test_case = int(input())

skill = list(input().rstrip())

LR = []
SK = []
cnt = 0

for i in skill :
    if i == 'S' :
        SK.extend(i)
    elif i == 'K' :
        if not SK :
            break
        else :
            SK.pop()
            cnt += 1

    elif i == 'L' :
        LR.extend(i)
    elif i == 'R' :
        if not LR :
            break
        else :
            LR.pop()
            cnt += 1
    else :
        cnt += 1

print(cnt)
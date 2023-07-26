import sys

input = sys.stdin.readline

test_case = int(input())

skill = list(input().rstrip())

LR = []
SK = []
cnt = 0

for i in skill :
    if i == 'S' :
        SK.append(i)
    elif i == 'K' :
        if not SK :
            break
        elif SK :
            SK.pop()
            cnt += 1

    elif i == 'L' :
        LR.append(i)
    elif i == 'R' :
        if not LR :
            break
        elif LR :
            LR.pop()
            cnt += 1
    else :
        cnt += 1

print(cnt)
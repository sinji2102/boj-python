import sys

input = sys.stdin.readline

crane = int(input().rstrip())
cranes = list(map(int, input().rstrip().split()))
box = int(input().rstrip())
boxes = list(map(int, input().rstrip().split()))
cnt = 0

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if max(cranes) < max(boxes) :
    print(-1)
else :
    while boxes :
        cnt += 1
        for i in range(len(cranes)) :
            # 원래 이 부분을 그냥 box로 넣었는데, 그럼 box에서 pop한 갯수를 카운트하지 못해서 인덱스 에러남
            for j in range(len(boxes)) :
                if cranes[i] >= boxes[j] :
                    boxes.pop(j)
                    break

    print(cnt)
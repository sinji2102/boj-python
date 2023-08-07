import sys

input = sys.stdin.readline

test_case = int(input().rstrip())

for _ in range(test_case) :
    people = int(input().rstrip())
    score = []
    cnt = 1
    first = 0

    for __ in range(people) :
        score.append(list(map(int, input().rstrip().split())))

    score.sort(key = lambda x : x[0])

    for i in range(len(score)) :
        # 어차피 이미 정렬된 상태이므로 면접 성적만 확인하면 됨!!
        if score[i][1] < score[first][1] :
            cnt += 1
            first = i

    print(cnt)
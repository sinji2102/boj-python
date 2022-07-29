N = int(input())

score = list(map(int, input().split()))
M = max(score)

for i in range(N) :
    score[i] = score[i] / M * 100

ave = 0
for j in score :
    ave += j

print(ave/N)
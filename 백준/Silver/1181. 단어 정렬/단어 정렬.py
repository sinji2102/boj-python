import sys
input = sys.stdin.readline

test_c = int(input())

word = []
for i in range(test_c) :
    word.append(input().strip())

word_ = list(set(word))

word_.sort()
word_.sort(key=len)

for j in  word_ :
    print(j)
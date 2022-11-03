import sys
input = sys.stdin.readline

row, col = map(int, input().rstrip().split())

list1_ = []
list2_ = []

for a in range(row) :
    list1_.append(list(map(int, input().rstrip().split())))

for b in range(row) :
    list2_.append(list(map(int, input().rstrip().split())))

for i in range(row) :
    for j in range(col) :
        list1_[i][j] = list1_[i][j] + list2_[i][j]


for pr in list1_ :
    for pr_ in pr :
        print(pr_, end = " ")
    print()
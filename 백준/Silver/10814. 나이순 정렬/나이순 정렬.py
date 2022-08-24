import sys
input = sys.stdin.readline

test_c = int(input())

list_ = []
for i in range(test_c) :
    age, name = map(str, input().rstrip().split())
    age = int(age)
    list_.append((age, name))

list_.sort(key = lambda x : x[0])

for j in list_ :
    print(j[0], j[1] )


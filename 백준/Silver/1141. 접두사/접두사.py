import sys

input = sys.stdin.readline
test_case = int(input().rstrip())
list_ = []
# cnt = 0
cnt = test_case

for _  in range(test_case) :
    list_.append(input().rstrip())

list_.sort(key = lambda x : len(x))

for i in range(test_case) :
    for j in range(i+1, test_case) :
        if list_[i] == list_[j][:len(list_[i])] :
            cnt -= 1
            break
    
print(cnt)
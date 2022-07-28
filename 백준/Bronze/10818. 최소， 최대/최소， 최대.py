A = input()

list_= list(map(int, input().split()))

list_.sort()
print(list_[0], list_[-1])

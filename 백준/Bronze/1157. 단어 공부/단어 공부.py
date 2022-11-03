A = input()
A = A.upper()
A_ = list(set(A))
list_ = []

for i in A_ :
    cnt = A.count(i)
    list_.append(cnt)

if list_.count(max(list_)) > 1 :
    print("?")
else : 
    index_ = list_.index(max(list_))
    print(A_[index_])
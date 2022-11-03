list_ = []

for i in range(10) :
    a = int(input())

    list_.append(a%42)

    set_ = set(list_)
    list_ = list(set_)

print(len(list_))
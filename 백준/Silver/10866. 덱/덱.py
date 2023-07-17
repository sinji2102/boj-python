import sys

input = sys.stdin.readline

test_case = int(input())
list_ = []

for _ in range(test_case):
    cmt = input()
    if "push" in cmt:
        if "back" in cmt :
            list_.append(int(cmt.split(' ')[-1]))
        else :
            x = int(cmt.split(' ')[-1])
            list_.insert(0, x)
            # print(x)
            # print(type(x))
    
    
    elif "pop" in cmt :
        if not list_ :
                print(-1)
        else :
            if "front" in cmt:
                    print(list_.pop(0))
            else :
                print(list_.pop(-1))

    cmt = cmt.rstrip()
    if cmt == "size":
        print(len(list_))
    elif cmt == "empty":
        if not list_ :
            print(1)
        else :
            print(0)
    elif cmt == "front":
        if not list_ :
            print(-1)
        else :
            print(list_[0])
    elif cmt == "back":
        if not list_ :
            print(-1)
        else :
            print(list_[-1])


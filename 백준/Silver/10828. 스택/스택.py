import sys

def poop(list_) :
    if len(list_) == 0 :
        print(-1)
    else :
        print(list_[-1])

list_ = []

for i in range(int(sys.stdin.readline())) :
    com = sys.stdin.readline().split()
    order = com[0]

    if order == "pop" :
        poop(list_)
        if len(list_) != 0 :
            del list_[-1]

    elif order == "size" :
        print(len(list_))
    
    elif order == "empty" :
        if len(list_) == 0 :
            print(1)
        else :
            print(0)
    
    elif order == "top" :
        if len(list_) == 0 :
            print(-1)
        else :
            print(list_[-1])
    
    else :
        list_.append(int(com[1]))
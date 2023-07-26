import sys

input = sys.stdin.readline

test_case = int(input())

for i in range(test_case) :
    list_ = input().rstrip()
    # print(list_)
    save = []
    right = 0
    
    for q in list_ :
        
        # print(q)

        if q == '(' :
            save.append('F')
            # print(save)
        elif q == ')' and save :
            save.pop()
            # print(save)
        else :
            print("NO")
            right += 1
            break
    
    if len(save) != 0 :
        print("NO")
    elif right == 0 :
        print("YES")
        right = 0


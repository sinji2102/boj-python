import sys

input = sys.stdin.readline

sen = list(input().rstrip())
sen2 = []
test_case = int(input())

for i in range(test_case) :
    list_ = list(input().rstrip().split())
    if len(list_) == 1 :
        if list_[0] == 'D' and sen2:
            sen.append(sen2.pop())
            # print(sen)
        elif list_[0] == 'L' and sen:
            sen2.append(sen.pop())
            # print(sen)
        elif list_[0] == 'B' and sen:
            sen.pop()
            # print(sen)
        
    else :
        sen.append(list_[-1])
        
        # print(sen)

sen = sen + sen2[::-1]

print("".join(map(str,sen)).rstrip())

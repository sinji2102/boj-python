import sys

ipt = sys.stdin.readline().rstrip()

list_ = []
result = 0
i = 0

while True :
    if i == len(ipt) :
        break
    if ipt[i] == '(' and ipt[i+1] != ')' :
        list_.append('F')
    elif ipt[i] == '(' and ipt[i+1] == ')' :
        result += len(list_) 
        i += 1
    elif ipt[i] == ')' and ipt[i-1] :
        del list_[-1]
        result += 1

    i += 1

print(result)


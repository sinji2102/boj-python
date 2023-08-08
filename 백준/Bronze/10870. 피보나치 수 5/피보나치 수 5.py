import sys

input = sys.stdin.readline

test_case = int(input().rstrip())

num1 , num2 = 0, 1
answer = 0 

for i in range(test_case) :
    if i == 0 :
        pass 
    else :
        answer = num1 + num2
        num1 = num2
        num2 = answer


if test_case == 1 :
    print(1)
else :
    print(answer)
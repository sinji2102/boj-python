import sys

input = sys.stdin.readline

test_case = int(input())
sen = input().rstrip()
num_list = []
result_list = []

for _ in range(test_case):
    num_list.append(int(input().rstrip()))

for alpha in sen :
    if 'A' <= alpha <= 'Z' :
        result_list.append(num_list[ord(alpha) - ord('A')])
    
    else : 
        # 무조건 num2 먼저 빼기!!!
        num2 = result_list.pop()
        num1 = result_list.pop()

        if alpha == '+' :
            result_list.append(num1 + num2)
        elif alpha ==  '-' :
            result_list.append(num1 - num2)
        elif alpha ==  '*' :
            result_list.append(num1 * num2)
        elif alpha ==  '/' :
            result_list.append(num1 / num2)

# print(round(float(result_list[0]), 3))
print(format(result_list[0],".2f"))

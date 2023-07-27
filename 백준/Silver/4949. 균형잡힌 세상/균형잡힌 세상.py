import sys

input = sys.stdin.readline

while True :
    sen = list(input().rstrip())
    # if문 아래 쓰면 메모리 차원에서 좋겠지만 난 예쁜 코드가 좋으니까...
    stack = []

    if len(sen) == 1 and sen[0] == '.' :
        break

    for i in sen :
        # print(stack)
        if i == '(' or i == '[' :
            stack.append(i)
        elif i == ')' :
            if stack and stack[-1] == '(' :
                stack.pop()
            else :
                stack.append(i)
                break
        elif i == ']' :
            if stack and stack[-1] == '[' :
                stack.pop()
            else :
                stack.append(i)
                break

    if not stack :
        print('yes')
    else :
        print('no')
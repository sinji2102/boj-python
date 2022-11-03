import sys
input = sys.stdin.readline

while True :
    # strip() 안 써서 개고생했다............... 꼭 쓰기 ^__^
    num = int(input().strip())
    
    if num == 0 :
        break

    num = str(num)
    
    if num == num[::-1] :
        print("yes")
    else :
        print("no")
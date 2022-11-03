import sys

input = sys.stdin.readline

pal = input().strip()

check = False
for i in range(len(pal)) :
    if pal[i] == pal[0] :
        check = True
    else : 
        check = False
        break

if check == True or len(pal) == 1 :
    print(-1)
elif pal == pal[::-1] :
    print(len(pal)-1)
else :
    print(len(pal))
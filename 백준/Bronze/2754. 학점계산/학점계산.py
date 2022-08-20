A = input()

cnt = 0

if A == "F" :
    A = "F0"
elif A[0] == "A" :
    cnt += 4
elif A[0] == "B" :
    cnt += 3
elif A[0] == "C" :
    cnt += 2
elif A[0] == "D" :
    cnt += 1

if A[1] == "+" :
    cnt += 0.3
elif A[1] == "-" :
    cnt -= 0.3
elif A[1] == "0" :
    cnt += 0.0

print(cnt)
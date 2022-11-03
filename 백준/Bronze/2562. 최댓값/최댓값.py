big = 0
cnt = 0

for i in range(9) :
    a = int(input())
    if a > big :
        big = a
        cnt = i
  
print(big)
print(cnt+1)
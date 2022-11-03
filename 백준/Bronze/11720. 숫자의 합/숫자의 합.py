cnt = int(input())

n = int(input())
sum = 0

for i in range(cnt) :
    sum += n % 10
    n = n // 10 

print(sum)
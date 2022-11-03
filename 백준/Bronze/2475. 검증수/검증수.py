a = list(map(int, input().split()))
num = 0

for i in a :
    num += i*i

print(num%10)
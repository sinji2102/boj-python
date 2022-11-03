import sys

input = sys.stdin.readline

test_c = int(input().rstrip())

nums = []
for i in range(test_c) :
    num = int(input().strip())

    if num == 0 :
        nums.pop()
    else :
        nums.append(num)

sum = 0
for j in nums :
    sum += j

print(sum)
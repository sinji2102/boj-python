import sys

input = sys.stdin.readline

A, B, C, M = map(int, input().split())

fatigue = 0  
work = 0     

for hour in range(24):
    if fatigue + A <= M:
        fatigue += A
        work += B
    else:
        fatigue = max(0, fatigue - C)

print(work)

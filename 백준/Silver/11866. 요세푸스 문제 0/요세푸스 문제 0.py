import sys

n, k = map(int, sys.stdin.readline().split())

idx = 0
queue = [i for i in range(1, n+1)]
res = []
while queue:
    idx += k - 1  
    if idx >= len(queue):  
        idx %= len(queue)  
    res.append(str(queue.pop(idx)))  

# 결과 출력
print("<", ", ".join(res), ">", sep="")
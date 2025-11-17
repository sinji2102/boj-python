import sys
input = sys.stdin.readline

N, R, Q = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

subtree = [0] * (N + 1)
parent = [0] * (N + 1)

# (현재 노드, 부모, 방문 상태)
# 방문 상태: 0=자식 방문 전, 1=자식 방문 후 계산 단계
stack = [(R, 0, 0)]  

order = []  # 자식 먼저 방문하기 위해 실제 방문 순서 기록
while stack:
    node, par, state = stack.pop()
    if state == 0:
        parent[node] = par
        stack.append((node, par, 1))   # 자식 처리 후 계산하도록
        for nxt in graph[node]:
            if nxt != par:
                stack.append((nxt, node, 0))
    else:
        # 자식이 모두 계산되면
        subtree[node] = 1
        for nxt in graph[node]:
            if nxt != par:
                subtree[node] += subtree[nxt]

for _ in range(Q):
    print(subtree[int(input())])

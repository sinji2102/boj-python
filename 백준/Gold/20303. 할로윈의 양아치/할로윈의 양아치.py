import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
candies = list(map(int, input().split()))

# 친구 관계 그래프 (인접 리스트)
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

# DFS
visited = [False] * N
components = []  # (size, candy_sum)

def dfs(node):
    stack = [node]
    total_candy = 0
    size = 0
    visited[node] = True
    while stack:
        u = stack.pop()
        total_candy += candies[u]
        size += 1
        for v in graph[u]:
            if not visited[v]:
                visited[v] = True
                stack.append(v)
    return (size, total_candy)

for i in range(N):
    if not visited[i]:
        components.append(dfs(i))


# dp[i] = 울음 수 i 이하일 때 최대 사탕 수
dp = [0] * K

for size, candy_sum in components:
    # size >= K 인 그룹은 선택 불가
    if size >= K:
        continue
    # 역순으로 업데이트 (중복 선택 방지)
    for i in range(K-1, size-1, -1):
        if dp[i - size] + candy_sum > dp[i]:
            dp[i] = dp[i - size] + candy_sum

print(max(dp))

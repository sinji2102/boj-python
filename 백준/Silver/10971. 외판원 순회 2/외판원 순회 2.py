import sys
input = sys.stdin.readline

N = int(input().strip())
W = [list(map(int, input().split())) for _ in range(N)]

INF = 10**18
FULL = (1 << N) - 1

dp = [[INF] * N for _ in range(1 << N)]     # dp[mask][i] = mask 상태에서 마지막이 i일 때의 최소 비용
start = 0
dp[1 << start][start] = 0

for mask in range(1 << N):
    for i in range(N):
        if dp[mask][i] == INF:
            continue
        # i에서 아직 방문하지 않은 j
        for j in range(N):
            if mask & (1 << j):
                continue  # 이미 방문
            if W[i][j] == 0:
                continue  # 갈 수 없음
            nm = mask | (1 << j)
            cost = dp[mask][i] + W[i][j]
            if cost < dp[nm][j]:
                dp[nm][j] = cost

# 모든 도시 방문 후 출발지로 돌아오는 경우 고려
ans = INF
for i in range(N):
    if dp[FULL][i] == INF:
        continue
    if W[i][start] == 0:
        continue
    ans = min(ans, dp[FULL][i] + W[i][start])

print(ans)

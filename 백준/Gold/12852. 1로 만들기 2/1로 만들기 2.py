import sys

input = sys.stdin.readline

N = int(input())

def one_dp(N):
    dp = [0] * (N + 1)
    prev = [0] * (N + 1)

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + 1
        prev[i] = i - 1

        # 연산 횟수 확인해서 저장
        if i % 2 == 0 and dp[i // 2] + 1 < dp[i]:
            dp[i] = dp[i // 2] + 1
            prev[i] = i // 2
        if i % 3 == 0 and dp[i // 3] + 1 < dp[i]:
            dp[i] = dp[i // 3] + 1
            prev[i] = i // 3

    path = []
    x = N
    while x != 0:
        path.append(x)
        if x == 1:
            break
        x = prev[x]

    return dp[N], path

count, path = one_dp(N)
print(count)
print(*path)

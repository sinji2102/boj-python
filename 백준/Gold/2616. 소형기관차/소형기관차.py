import sys

input = sys.stdin.readline

N = int(input())  # 객차 수
passenger = list(map(int, input().split()))  # 객차 손님 수
M = int(input())  # 소형 기관차가 끌 수 있는 객차 수

# 누적합
prefix = [0] * (N + 1)
for i in range(1, N + 1):
    # 각 구간의 손님 수를 계산한 누적합 배열
    prefix[i] = prefix[i - 1] + passenger[i - 1] 

# dp[k][i]: k번째 기관차까지 고려했을 때 i번째 객차까지 운송할 수 있는 최대 손님 수
dp = [[0] * (N + 1) for _ in range(4)]  # 기관차는 1~3

for k in range(1, 4):
    for i in range(k * M, N + 1):
        # 이번 객차 포함 x / 이번 객차 포함 구간까지 비교하여 max값 확인
        dp[k][i] = max(dp[k][i - 1], dp[k - 1][i - M] + (prefix[i] - prefix[i - M]))
        # print(dp)

print(dp[3][N])

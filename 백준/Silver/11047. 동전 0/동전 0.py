# https://www.acmicpc.net/problem/11047

# 1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수라는 조건이 있기 때문에 greedy로 풀이

import sys

input = sys.stdin.readline

N, K = map(int, input().split())

# coins 배열에 동전의 종류들 넣기
coins = []
for i in range(N) :
    coin = int(input())
    coins.append(coin)

cnt = 0 # 필요한 동전의 개수

while True:
    # 동전으 큰 것부터 비교하여 동전이 더 작으면 
    for i in reversed(coins) : 
        if K >= i :
            K -= i  # 해당 동전 값만큼 빼고
            cnt += 1    # 동전 개수 추가
            break
    
    # 값이 0이 되면 종료
    if K == 0 :
        break

print(cnt)
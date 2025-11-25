import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

dirs = [(-1,0), (1,0), (0,-1), (0,1)]

for _ in range(T):
    R, C = map(int, input().split())
    grid = [list(input().split()) for _ in range(R)]

    # visited[r][c] = r,c에 도달하기 위해 부숴야 하는 최소 울타리 수
    visited = [[-1] * C for _ in range(R)]  # 기본은 방문하지 않은 것 (-1)으로 세팅
    dq = deque()

    for r in range(R):
        for c in range(C):
            if r == 0 or r == R-1 or c == 0 or c == C-1:    # 외곽이 0이면 비용 0, 1이면 비용 1로 시작
                if grid[r][c] == '0':    # 비용이 0이면 우선 탐색 (앞에 넣기)
                    visited[r][c] = 0
                    dq.appendleft((r, c))
                else:   # 비용이 1이면 나중에 탐색 (뒤에 넣기)
                    visited[r][c] = 1
                    dq.append((r, c))

    while dq:
        r, c = dq.popleft()

        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            
            if 0 <= nr < R and 0 <= nc < C:
                # 다음 칸으로 갈 때 드는 추가 비용 계산
                cost = 1 if grid[nr][nc] == '1' else 0
                new_cost = visited[r][c] + cost

                # 아직 방문하지 않았거나, 더 적은 비용으로 도달할 수 있다면 갱신
                if visited[nr][nc] == -1 or visited[nr][nc] > new_cost:
                    visited[nr][nc] = new_cost
                    
                    # 비용이 0인 간선은 앞에, 1인 간선은 뒤에 추가
                    if cost == 0:
                        dq.appendleft((nr, nc))
                    else:
                        dq.append((nr, nc))

    max_break = 0 
    
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '0' and visited[r][c] != -1:
                if visited[r][c] > max_break:
                    max_break = visited[r][c]

    flower = 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == '0' and visited[r][c] == max_break:
                flower += 1

    print(max_break, flower)
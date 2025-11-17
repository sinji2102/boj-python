import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]

# 각 빈 공간(0)의 연결 요소 크기를 기록하는 배열
comp_size = []
comp_id = [[-1] * M for _ in range(N)]

# 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# BFS로 연결된 0 구역을 찾고 comp_id에 번호 기록
def bfs(sx, sy, idx):
    q = deque([(sx, sy)])
    comp_id[sx][sy] = idx
    size = 1

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M:
                if board[nx][ny] == 0 and comp_id[nx][ny] == -1:
                    comp_id[nx][ny] = idx
                    q.append((nx, ny))
                    size += 1

    return size


# 빈 공간 구역들을 전부 파악해서 comp_id, comp_size 채움
idx = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 0 and comp_id[i][j] == -1:
            size = bfs(i, j, idx)
            comp_size.append(size)
            idx += 1

result = [[0] * M for _ in range(N)]

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:     # 벽이라면
            seen = set()
            total = 1            # 벽을 부쉈을 때 자기 자신 포함

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]

                if 0 <= nx < N and 0 <= ny < M:
                    cid = comp_id[nx][ny]
                    if cid != -1 and cid not in seen:
                        seen.add(cid)
                        total += comp_size[cid]

            result[i][j] = total % 10

        else:
            result[i][j] = 0

for i in range(N):
    print("".join(map(str, result[i])))

import sys, math
input = sys.stdin.readline


def find(parent, x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(parent, rank, a, b):
    ra = find(parent, a)
    rb = find(parent, b)
    if ra == rb:
        return False
    if rank[ra] < rank[rb]:
        parent[ra] = rb
    else:
        parent[rb] = ra
        if rank[ra] == rank[rb]:
            rank[ra] += 1
    return True


N, M = map(int, input().split())
points = [tuple(map(int, input().split())) + (i,) for i in range(N)]  # (x, y, index)

edges = []

# 이미 존재하는 M개의 통로 구하기
for _ in range(M):
    u, v = map(int, input().split())
    u -= 1  # 0-based index
    v -= 1
    edges.append((0.0, u, v))  # 기존 통로는 길이 0

# 모든 가능한 새로운 간선
for i in range(N):
    x1, y1, idx1 = points[i][:3]
    for j in range(i+1, N):
        x2, y2, idx2 = points[j][:3]
        dist = math.hypot(x1 - x2, y1 - y2)
        edges.append((dist, idx1, idx2))

# MST
edges.sort(key=lambda e: e[0])
parent = list(range(N))
rank = [0] * N
total_length = 0.0
used_edges = 0

for cost, u, v in edges:
    if union(parent, rank, u, v):
        total_length += cost
        used_edges += 1
        if used_edges == N - 1:
            break

print(f"{total_length:.2f}")

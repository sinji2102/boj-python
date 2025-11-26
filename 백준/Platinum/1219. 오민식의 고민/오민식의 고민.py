import sys
from collections import deque
input = sys.stdin.readline

INF_NEG = -10**18

N, S, E, M = map(int, input().split())
edges = []
graph = [[] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))
    graph[u].append(v)

earn = list(map(int, input().split()))

# dist[i] = 출발지에서 i에 도달했을 때 가질 수 있는 최대 금액
dist = [INF_NEG] * N
dist[S] = earn[S]

for _ in range(N - 1):
    updated = False
    for u, v, w in edges:
        if dist[u] == INF_NEG:
            continue
        cand = dist[u] - w + earn[v]
        if cand > dist[v]:
            dist[v] = cand
            updated = True
    if not updated:
        break

# N번째 반복에서 갱신 가능한 노드 수집
cycle_nodes = [False] * N
for u, v, w in edges:
    if dist[u] == INF_NEG:
        continue
    cand = dist[u] - w + earn[v]
    if cand > dist[v]:
        cycle_nodes[v] = True

# cycle_nodes 에서 전파: 사이클로부터 도달 가능한 모든 노드 표시 -> 간선 방향을 따라 전파하여 확장되는 노드들 찾기!!
q = deque([i for i, val in enumerate(cycle_nodes) if val])
visited_cycle_reach = [False] * N
for i in q:
    visited_cycle_reach[i] = True

while q:
    u = q.popleft()
    for v in graph[u]:
        if not visited_cycle_reach[v]:
            visited_cycle_reach[v] = True
            q.append(v)

if visited_cycle_reach[E]:
    print("Gee")
elif dist[E] == INF_NEG:
    print("gg")
else:
    print(dist[E])

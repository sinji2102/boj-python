import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input().strip())
    last = list(map(int, input().split())) 
    m = int(input().strip())

    adj = [[False]*(n+1) for _ in range(n+1)]   # 인접 행렬(혹은 집합)과 indegree
    indeg = [0]*(n+1)

    # 작년 순위를 바탕으로 모든 i<j에 대해 last[i] -> last[j]
    for i in range(n):
        for j in range(i+1, n):
            u = last[i]
            v = last[j]
            if not adj[u][v]:
                adj[u][v] = True
                indeg[v] += 1

    # 두 팀 사이 간선 뒤집기
    for _ in range(m):
        a, b = map(int, input().split())
        # 만약 a->b 가 있으면 b->a로, 아니면 a->b로
        if adj[a][b]:
            adj[a][b] = False
            indeg[b] -= 1
            if not adj[b][a]:
                adj[b][a] = True
                indeg[a] += 1
        elif adj[b][a]:
            adj[b][a] = False
            indeg[a] -= 1
            if not adj[a][b]:
                adj[a][b] = True
                indeg[b] += 1

    # 위상정렬
    # 동시에 진입차수 0인 노드가 2개 이상이면 불확실
    q = deque()
    for i in range(1, n+1):
        if indeg[i] == 0:
            q.append(i)

    result = []
    ambiguous = False
    impossible = False

    for _iter in range(n):
        if not q:
            impossible = True
            break
        if len(q) > 1:
            ambiguous = True
        u = q.popleft()
        result.append(u)
        for v in range(1, n+1):
            if adj[u][v]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

    if impossible:
        print("IMPOSSIBLE")
    elif ambiguous:
        print("?")
    else:
        print(" ".join(map(str, result)))

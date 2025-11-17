import sys
input = sys.stdin.readline


class DSU:
    def __init__(self, n):
        # parent[i] = i의 부모 - 처음에는 자기 자신이어야 함!!! 
        self.parent = list(range(n))
        # rank는 트리 높이를 나타내는 보조 배열 -> union-by-rank에 사용
        self.rank = [0] * n

    def find(self, x):
        # while문으로 부모를 따라가며 루트까지 도달하고, 지나온 노드들의 parent를 루트로 직접 연결
        while self.parent[x] != x:
            # 부모의 부모로 한 단계 압축
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a, b):
        # a와 b를 합친다 (이미 같은 집합이면 False 반환!!)
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return False

        # rank 기준으로 루트를 붙여서 트리 높이 증가를 억제
        if self.rank[ra] < self.rank[rb]:
            self.parent[ra] = rb
        else:
            self.parent[rb] = ra
            if self.rank[ra] == self.rank[rb]:
                self.rank[ra] += 1
        return True

def MST():
    # 행성 수 입력
    N = int(input().strip())

    # 각 행성의 좌표와 인덱스 저장: (x, y, z, index)
    # index는 Union-Find에서 사용하는 정점 번호로 사용
    points = []
    for i in range(N):
        x, y, z = map(int, input().split())
        points.append((x, y, z, i))

    # 모든 후보 간선을 담을 리스트 (cost, u_index, v_index)
    edges = []

    # 관찰: 비용이 min(|dx|,|dy|,|dz|) 이므로 각 축(x/y/z) 별로 정렬한 후에 '인접한' 점들만 후보 간선으로 추가해도 MST를 구성하는 데 충분함
    # -> 그렇게 하면 간선 수가 3*(N-1)로 줄어 계산 가능함!!!

    # x 좌표 기준으로 정렬 후 인접한 쌍을 edge로 추가
    pts_x = sorted(points, key=lambda p: p[0])  # x 기준 오름차순
    for i in range(N - 1):
        a = pts_x[i]
        b = pts_x[i + 1]

        cost = min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))     # 비용은 세 좌표 차이의 최소값
        edges.append((cost, a[3], b[3]))  # (cost, index_u, index_v)

    # y 좌표 기준으로 정렬 후 인접한 쌍을 edge로 추가
    pts_y = sorted(points, key=lambda p: p[1])  # y 기준 오름차순
    for i in range(N - 1):
        a = pts_y[i]
        b = pts_y[i + 1]
        cost = min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))
        edges.append((cost, a[3], b[3]))

    # z 좌표 기준으로 정렬 후 인접한 쌍을 edge로 추가
    pts_z = sorted(points, key=lambda p: p[2])  # z 기준 오름차순
    for i in range(N - 1):
        a = pts_z[i]
        b = pts_z[i + 1]
        cost = min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))
        edges.append((cost, a[3], b[3]))


    # MST
    # 1) 간선을 비용 기준으로 오름차순 정렬
    # 2) 작은 비용 간선부터 Union-Find로 연결 (사이클 방지를 위해서)
    # 3) N-1개의 간선을 선택하면 종료
    edges.sort(key=lambda e: e[0])  # 비용 기준 정렬
    dsu = DSU(N)

    total_cost = 0  # MST의 총 비용
    used = 0        # 현재까지 선택한 간선 수

    for cost, u, v in edges:
        # u와 v가 서로 다른 컴포넌트라면 합치고 비용 더하기
        if dsu.union(u, v):
            total_cost += cost
            used += 1
            if used == N - 1:  # 이미 N-1개 간선을 사용하면 완성
                break

    print(total_cost)

MST()

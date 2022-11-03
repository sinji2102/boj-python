import sys

input = sys.stdin.readline

A, B, V = map(int, input().split())

# 달팽이가 하루에 A-B만큼 올라가고, 올라가야 하는 길이는 V-B
# 올라가야 하는 길이 / 하루에 올라가는 길이
if (V - B) % (A - B) == 0 : 
    print((V - B) // (A - B))
else :
    # 나머지가 0이 아니라면 하루가 더 필요함 : +1 해주기
    print((V - B) // (A - B) + 1)

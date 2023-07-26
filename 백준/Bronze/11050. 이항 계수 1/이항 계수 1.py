import sys

input = sys.stdin.readline

n, k = map(int, input().split())

n_a = 1
k_a = 1
nk_a = 1

for i in range(1, n+1) :
    n_a *= i

for j in range(1, k+1) :
    k_a *= j

for q in range(1, n-k+1):
    nk_a *= q

print(int(n_a/nk_a/k_a))
import sys
input = sys.stdin.readline

L = int(input().strip())
S = input().strip()

def get_pi(S):
    pi = [0] * L
    j = 0
    for i in range(1, L):
        while j > 0 and S[i] != S[j]:
            j = pi[j-1]
        if S[i] == S[j]:
            j += 1
            pi[i] = j
    return pi

pi = get_pi(S)

ans = L - pi[L-1]

print(ans)
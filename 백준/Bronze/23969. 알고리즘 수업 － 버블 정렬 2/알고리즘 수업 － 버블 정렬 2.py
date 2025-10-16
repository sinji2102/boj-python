import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

def bubble_sort(arr):
    cnt = 0

    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt +=1
            if cnt == K:
                print(*arr)
                return

    if cnt < K:
        print(-1)

bubble_sort(arr)
import sys

sys.setrecursionlimit(int(1e4))
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

def partition(arr, left, right):
    global cnt
    pivot = arr[right]    # 기준 원소(피벗)
    i = left - 1

    for j in range(left, right):
        # 피벗보다 작은 원소일 경우 교환 + i값 증가
        # 피벗보다 큰 원소일 경우 교환 X -> 배열을 그대로 유지해야 하기 때문에
        if arr[j] <= pivot:
            cnt += 1
            i += 1  
            
            arr[i], arr[j] = arr[j], arr[i]

            if cnt == K:
                print(*sorted([arr[i], arr[j]]))
                return -1

    # 피벗을 i 위치로 옮기기(올바른 자리에 위치하도록 하기)
    if i + 1 != right:
        # 피벗을 i 위치로 옮기는 교환까지 카운트
        cnt += 1
        arr[i + 1], arr[right] = arr[right], arr[i + 1]

        # K값이 마지막 교환 횟수와 같을 경우
        if cnt == K:
            print(*sorted([arr[i + 1], arr[right]]))
            return -1

    return i + 1 

def quick_sort(arr, left, right):
    if left < right:
        p = partition(arr, left, right)

        if p == -1:
            return

        quick_sort(arr, left, p - 1)
        quick_sort(arr, p + 1, right)

    return arr

quick_sort(arr, 0, N-1)

if cnt < K:
    print(-1)

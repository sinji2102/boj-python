import sys

sys.setrecursionlimit(int(1e4))
input = sys.stdin.readline

N, Q, K = map(int, input().split())
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
            i += 1  
            
            arr[i], arr[j] = arr[j], arr[i]
            
            cnt += 1
            if cnt == K:
                print(*arr)
                return -2
                        
        # print(cnt, arr)

    # 피벗을 i 위치로 옮기기(올바른 자리에 위치하도록 하기)
    if i + 1 != right:
        # 피벗을 i 위치로 옮기는 교환까지 카운트
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        cnt += 1

        # print("test", cnt, arr)

        # if i+1 == Q and cnt != K:
        #     cnt -= 1
        #     return -1

        # K값이 마지막 교환 횟수와 같을 경우
        if cnt == K:
            print(*arr)
            return -2
        
    return i + 1 

def select(arr, left, right, q):
    if (left == right) :
        return arr[left]

    p = partition(arr, left, right)

    if p == -2 :
        return
    
    k = p - left + 1

    if (q < k) :
        select(arr, left, p - 1, q)
    elif (q == k) :
        return arr[p]
    else :
        select(arr, p + 1, right, q-k)

    return arr

select(arr, 0, N-1, Q)

if cnt < K:
    print(-1)

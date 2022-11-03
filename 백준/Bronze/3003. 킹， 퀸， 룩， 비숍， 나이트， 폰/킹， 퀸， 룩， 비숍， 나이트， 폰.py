x = list(map(int, input().split()))
y = [1, 1, 2, 2, 2, 8]

for i in range(len(x)) :
    print(y[i] - x[i], end = " ")
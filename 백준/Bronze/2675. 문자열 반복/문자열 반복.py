test_c = int(input())

for c in range(test_c):
    A, B = input().split()
    for i in range(len(B)) :
            for j in range(int(A)) :
                print(B[i], end = "")
    print()
sang = list(map(int, input().split()))

for i in range(2) :
    sang[i] = ((sang[i] % 10) * 100) + ((sang[i] % 100 // 10) * 10) + (sang[i] // 100)

if sang[0] > sang[1]  :
    print(sang[0])
else :
    print(sang[1])
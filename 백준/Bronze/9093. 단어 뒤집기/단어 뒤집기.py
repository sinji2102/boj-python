test_c = int(input())

for i in range(test_c) :
    txt = input()
    txt_list = txt.split()
    
    cnt = len(txt_list)

    for j in range(cnt) :
        txt_list[j] = txt_list[j][::-1]

    for n in range(cnt) :
        print(txt_list[n], end=" ")

    print()
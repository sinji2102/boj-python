test_c = int(input())

for i in range(test_c) :
    quiz = input()
    cnt = 0
    con = 0
    for j in range(len(quiz)) :
        if quiz[j] == "X" :
            con = 0
        else :
            con += 1
            cnt += con

    print(cnt)

test_c = int(input())

for i in range(test_c) :
    x = input()
    
    if len(x) == 1 :
        print(x*2)
    else :
        print(x[0]+x[-1])
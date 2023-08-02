import sys

input = sys.stdin.readline
word = input().rstrip()

answer = ['z' for i in range(len(word))]
answer = "".join(answer)


for i in range(1,len(word)-1) :
    for j in range(i+1, len(word)) :
        answer2 = ""
        word2 = word[:i]
        answer2 += word2[::-1]
        word2 = word[i:j]
        answer2 += word2[::-1]
        word2 = word[j:]
        answer2 += word2[::-1]

        if answer > answer2 :
            answer = answer2

print(answer)
import sys
from collections import deque
input = sys.stdin.readline
 
def main():
	n = int(input())
	seq = deque([int(input().strip()) for _ in range(n)])
	stack, answer = [0], []
	i = 1
	while seq:
		if stack[-1] == seq[0]:
			seq.popleft()
			stack.pop()
			answer.append("-")
		elif stack[-1] < seq[0]:
			stack.append(i)
			answer.append("+")
			i += 1
		elif stack[-1] > seq[0]:
			print("NO")
			return
	[print(a) for a in answer]
 
main()

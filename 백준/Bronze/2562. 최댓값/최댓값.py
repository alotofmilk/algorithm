import sys
answer = []
for i in range(9): answer.append(int(sys.stdin.readline()))
print(max(answer), answer.index(max(answer))+1, sep="\n")
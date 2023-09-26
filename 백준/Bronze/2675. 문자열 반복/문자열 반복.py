import sys
T = int(sys.stdin.readline()); answer = []
for i in range(0,T):
    data = ""
    R, S = map(str,sys.stdin.readline().split())
    for j in range(0,len(S)): data = data + int(R) * S[j]
    answer.append(data)
print(*answer, sep="\n")
import sys
T = int(sys.stdin.readline()); change = ""; answer = []
for i in range(T):
    words = list(map(str,sys.stdin.readline().split()))
    for j in range(len(words)):
        change += words[j][::-1] + " "
    answer.append(change); change = ""
print(*answer, sep="\n", end="\n")
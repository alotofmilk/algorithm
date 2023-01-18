import sys
T = int(sys.stdin.readline()); new_sentence = ""; answer = []
for i in range(T):
    R, S = map(str,sys.stdin.readline().split())
    for j in range(len(S)): new_sentence += int(R) * S[j]
    answer.append(new_sentence)
    new_sentence = ""
print(*answer, sep="\n")
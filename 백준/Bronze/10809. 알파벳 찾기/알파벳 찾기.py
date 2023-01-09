import sys
S = sys.stdin.readline().strip(); alphabet_count = []
for i in range(26): alphabet_count.append(-1)
for i in range(0,len(S)):
    if alphabet_count[ord(S[i])-ord('a')] > -1: pass
    else: alphabet_count[ord(S[i])-ord('a')] = i
print(*alphabet_count, end="")
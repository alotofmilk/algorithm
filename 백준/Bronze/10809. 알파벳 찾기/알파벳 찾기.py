import sys
S = sys.stdin.readline().strip()
alphabet = [-1 for i in range(26)]
for i in range(len(S)): alphabet[ord(S[i])-97] = S.find(S[i])
print(*alphabet)
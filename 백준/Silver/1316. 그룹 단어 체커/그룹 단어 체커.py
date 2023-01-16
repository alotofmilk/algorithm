import sys
N = int(sys.stdin.readline()); word = []; m = 0; n =0; yes_or_no = []; answer = []
for i in range(N): word.append(sys.stdin.readline())
for i in range(N):
    for j in range(len(word[i])):
        m = word[i].find(word[i][j])
        n = word[i].rfind(word[i][j])
        if m == n: pass
        elif m != n:
            for l in range(m,n-1):
                if word[i][l] == word[i][l+1]: pass
                else:
                    yes_or_no.append("no")
                    break
    if "no" in yes_or_no:
        answer.append(0)
        yes_or_no.clear()
print(N-answer.count(0))
import sys
N = int(sys.stdin.readline())
color_paper = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
paper = [[0] * 101 for i in range(101)]; result = 0
for i in range(N):
    for j in range(color_paper[i][0], color_paper[i][0] + 10):
        for k in range(color_paper[i][1], color_paper[i][1] + 10):
            if j <= len(paper) and k <= len(paper):
                if paper[j][k] == 0:
                    paper[j][k] = 1
                    result += 1
                else: pass
print(result)
N = int(input()); answer = []
for i in range(N):
    S, T = map(str, input().split())
    if S * len(T) == T * len(S): answer.append("yes")
    else: answer.append("no")
for i in range(N): print("#{} {}".format(i+1,answer[i]))
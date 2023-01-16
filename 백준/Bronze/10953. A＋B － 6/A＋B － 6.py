T = int(input()); answer = []
for i in range(T):
    A, B = map(int,input().split(","))
    answer.append(A+B)
print(*answer)
T = int(input()); answer = []
for i in range(T):
    N = int(input())
    numbers = list(map(int,input().split()))
    answer.append(sum(numbers))
print(*answer, sep="\n")
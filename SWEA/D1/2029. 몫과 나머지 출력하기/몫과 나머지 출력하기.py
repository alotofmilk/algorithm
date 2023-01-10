T = int(input()); answer = []
for i in range(T):
    a, b = map(int,input().split())
    answer.append(divmod(a,b))
for i in range(0,T): print("#{} {} {}".format(i+1,answer[i][0],answer[i][1]))
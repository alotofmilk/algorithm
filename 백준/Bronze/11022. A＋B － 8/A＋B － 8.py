import sys
T = int(sys.stdin.readline()); data = []
for i in range(0,T):
    A, B = map(int,sys.stdin.readline().split())
    data.append([A,B,A+B])
for i in range(0,T):
    print("Case #{}: {} + {} = {}".format(i+1, data[i][0], data[i][1], data[i][2]))
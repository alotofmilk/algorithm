import sys
N = sys.stdin.readline()
for i in range(len(N)):
    cnt = i
    if cnt != 0 and cnt % 10 == 0: print("\n{}".format(N[i]),sep="",end="")
    else: print(N[i],sep="",end="")
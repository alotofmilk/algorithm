import sys
N = int(sys.stdin.readline()); cute = 0; notCute = 0
for i in range(N):
    result = sys.stdin.readline().strip()
    if result == "0": notCute += 1
    else: cute += 1
if cute > notCute : print("Junhee is cute!")
else: print("Junhee is not cute!")
import sys
N = int(sys.stdin.readline())
result = sys.stdin.readline().strip(); countA = 0; countB = 0
for i in range(N):
    if result[i] == "A": countA += 1
    else: countB += 1
if countA > countB : print("A")
elif countA < countB : print("B")
else: print("Tie")
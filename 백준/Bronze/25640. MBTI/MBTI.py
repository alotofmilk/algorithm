import sys
Jinho = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip()); same = 0
friends = [sys.stdin.readline().strip() for i in range(N)]
for i in range(N):
    if friends[i] == Jinho: same += 1
print(same)
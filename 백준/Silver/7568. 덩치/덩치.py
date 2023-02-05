import sys
N = int(sys.stdin.readline().strip()); physical = []; rank = []
for i in range(N):
    weight, height = map(int,sys.stdin.readline().split())
    physical.append((weight,height))
    rank.append(1)
for i in range(0,N):
    for j in range(0,N):
        if physical[i][0] < physical[j][0] and physical[i][1] < physical[j][1]: rank[i] += 1
        else: pass
print(*rank)
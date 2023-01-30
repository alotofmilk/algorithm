import sys

plane = []; size = 0
for i in range(1,101):
    plane.append([0 for j in range(1,101)])

for i in range(4):
    where = list(map(int,sys.stdin.readline().split()))
    for j in range(where[0], where[2]):
        for k in range(where[1], where[3]):
            if plane[j][k] == 0: plane[j][k] += 1

for i in range(0,len(plane)):
    if 1 in plane[i]: size += plane[i].count(1)
print(size)
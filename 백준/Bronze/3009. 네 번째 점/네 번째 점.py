import sys
make_rectangle = [[],[]]; find_last_X = 0; find_last_Y = 0
for i in range(3):
    X, Y = map(int,sys.stdin.readline().split())
    make_rectangle[0].append(X)
    make_rectangle[1].append(Y)

if make_rectangle[0].count(max(make_rectangle[0])) > make_rectangle[0].count(min(make_rectangle[0])):
    find_last_X = min(make_rectangle[0])
else: find_last_X = max(make_rectangle[0])

if make_rectangle[1].count(max(make_rectangle[1])) > make_rectangle[1].count(min(make_rectangle[1])):
    find_last_Y = min(make_rectangle[1])
else: find_last_Y = max(make_rectangle[1])

print("{} {}".format(find_last_X, find_last_Y))
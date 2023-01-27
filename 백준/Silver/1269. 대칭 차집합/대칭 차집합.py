import sys
how_many_A, how_many_B = map(int,sys.stdin.readline().split())
A = set(list(map(int,sys.stdin.readline().split())))
B = set(list(map(int,sys.stdin.readline().split())))
result = A.union(B) - A.intersection(B)
print(len(result))
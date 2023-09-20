import sys
N, M = map(int, sys.stdin.readline().split())
if N == 1 and M == 1: print(0)
else: print(((M-1)+M*(N-1)))
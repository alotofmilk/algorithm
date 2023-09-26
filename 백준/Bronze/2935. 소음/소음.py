import sys
A = int(sys.stdin.readline())
cal = sys.stdin.readline().split()
B = int(sys.stdin.readline())
if cal[0] == "+": print(A+B)
else: print(A*B)
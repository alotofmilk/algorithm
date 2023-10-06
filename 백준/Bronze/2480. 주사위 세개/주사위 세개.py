import sys
A, B, C = map(int,sys.stdin.readline().split())
if A == B and B == C and C == A:
    print(10000 + A * 1000)
elif A == B and B != C:
    print(1000 + A * 100)
elif A != B and B == C:
    print(1000 + B * 100)
elif B != C and C == A:
    print(1000 + C * 100)
elif A != B and B != C and C != A:
    print(max(A,B,C) * 100)
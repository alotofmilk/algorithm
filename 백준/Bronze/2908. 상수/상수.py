import sys
A, B = map(int,sys.stdin.readline().split())
new_A = (A // 100) + (A % 100 // 10) * 10 + (A % 10) * 100
new_B = (B // 100) + (B % 100 // 10) * 10 + (B % 10) * 100
print(max(new_A, new_B))
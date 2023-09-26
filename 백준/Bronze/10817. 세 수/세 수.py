import sys
A,B,C = map(int,sys.stdin.readline().split()); list = [A,B,C]
list.remove(max(list))
print(max(list))
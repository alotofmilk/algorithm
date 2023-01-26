import sys
N = int(sys.stdin.readline())
seat = [0 for i in range(100)]; reject = 0
people = list(map(int,sys.stdin.readline().split()))
for i in range(len(people)):
    if seat[people[i]-1] == 0: seat[people[i]-1] += 1
    else: reject += 1
print(reject)
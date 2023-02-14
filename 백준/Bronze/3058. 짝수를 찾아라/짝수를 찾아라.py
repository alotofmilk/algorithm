import sys
T = int(sys.stdin.readline().strip()); even = []
for _ in range(T):
    numbers = list(map(int,sys.stdin.readline().split()))
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            even.append(numbers[i])
    print(sum(even),min(even))
    even.clear()
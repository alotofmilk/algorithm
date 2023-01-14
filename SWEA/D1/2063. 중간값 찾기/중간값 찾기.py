n = int(input());
numbers = list(map(int, input().split()))
numbers.sort()
print(numbers[(len(numbers) + 1) // 2 - 1])
N = int(input())
sum = (N // 1000) + ((N % 1000) // 100) + ((N % 100) // 10) + (N % 10)
print(sum)
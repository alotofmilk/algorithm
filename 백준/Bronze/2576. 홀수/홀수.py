odd_numbers = []
for i in range(7):
    number = int(input())
    if number % 2 == 1: odd_numbers.append(number)
if len(odd_numbers) == 0: print(-1)
else: print(sum(odd_numbers), min(odd_numbers), sep="\n")
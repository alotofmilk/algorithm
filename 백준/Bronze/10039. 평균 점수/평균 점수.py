import sys
result = []
for i in range(5):
    score = int(sys.stdin.readline())
    if score < 40: score = 40
    result.append(score)
print(sum(result) // 5)
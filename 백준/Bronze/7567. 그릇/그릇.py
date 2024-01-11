import sys
plate = sys.stdin.readline().strip()
tmp = plate[0]; height = 10
for i in range(1,len(plate)):
    if plate[i] == tmp:
        height += 5
        tmp = plate[i]
    else:
        height += 10
        tmp = plate[i]
print(height)
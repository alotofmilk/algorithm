import sys
word = sys.stdin.readline().strip(); count = []; find_max = 0; max_count = 0; max_index = 0
for i in range(26): count.append(0)
for i in range(len(word)):
    if 65 <= ord(word[i]) <= 90: count[ord(word[i])-65] += 1
    elif 97 <= ord(word[i]) <= 122: count[ord(word[i])-32-65] += 1
find_max = max(count)
for i in range(len(count)):
    if count[i] == find_max:
        max_count += 1
        max_index = i
    if max_count > 1: break
if max_count > 1: print("?")
else: print(chr(max_index+65))
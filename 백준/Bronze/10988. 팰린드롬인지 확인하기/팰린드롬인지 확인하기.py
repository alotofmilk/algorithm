import sys
word = sys.stdin.readline().strip()
reverse_word = word[::-1]; cnt = ""
for i in range(len(word)):
    if word[i] == reverse_word[i]: cnt += "*"
    else:
        print(0)
        break
if len(cnt) == len(word): print(1)
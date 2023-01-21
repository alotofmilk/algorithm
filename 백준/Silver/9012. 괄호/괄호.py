import sys
T = int(sys.stdin.readline())
for i in range(T):
    sentence = sys.stdin.readline().strip()
    while "()" or "*" in sentence:
        if "()" in sentence: sentence = sentence.replace("()", "*")
        elif "*" in sentence: sentence = sentence.replace("*", "")
        elif "()" or "*" not in sentence: break
    if len(sentence) == 0: print("YES")
    else: print("NO")
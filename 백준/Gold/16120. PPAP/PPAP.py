import sys
sentence = sys.stdin.readline().strip(); stack = []
for i in range(len(sentence)):
    stack.append(sentence[i])
    if "".join(stack[-4:]) == "PPAP":
        stack.pop()
        stack.pop()
        stack.pop()
        stack.pop()
        stack.append("P")
    else: pass
if len(stack) == 1 and stack[-1] == "P": print("PPAP")
else: print("NP")
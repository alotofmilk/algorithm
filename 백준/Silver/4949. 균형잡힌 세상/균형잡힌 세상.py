import sys
take_balance = {"(" : ")","[" : "]"}; tmp = ""
sentence = ""; stack = []
while True:
    sentence = sys.stdin.readline().rstrip()
    if sentence == ".": break
    else:
        for i in range(len(sentence)):
            if sentence[i] in take_balance.keys():
                stack.append(sentence[i])
            elif sentence[i] in take_balance.values():
                stack.append(sentence[i])
            else: pass
        for i in range(len(stack)):
            check_key = stack.count(take_balance.keys())
            check_value = stack.count(take_balance.values())
            if check_key != check_value:
                print("no")
                break
            else:
                tmp = "".join(stack)
                for j in range(len(stack)):
                    if "()" in tmp:
                        tmp = tmp.replace("()","")
                    if "[]" in tmp:
                        tmp = tmp.replace("[]","")
        if tmp == "":
            print("yes")
            tmp = ""
            stack.clear()
        else:
            print("no")
            tmp = ""
            stack.clear()
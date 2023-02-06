import sys
message = sys.stdin.readline()
smile = ":-)"; oops = ":-("
happy = message.count(smile)
sad = message.count(oops)
if happy == 0 and sad == 0: print("none")
elif happy > sad: print("happy")
elif happy < sad: print("sad")
else: print("unsure")
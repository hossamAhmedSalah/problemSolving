word = input()
upper = [w for w in word if w.isupper()]
lower = [w for w in word if w.islower()]
if len(upper) > len(lower):
    print(word.upper())
else:
    print(word.lower())

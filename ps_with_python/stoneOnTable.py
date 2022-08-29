input()
s = input()
z = list(zip(s[1:], s))
 
print(sum(a==b for a, b in zip(s[1:], s)))

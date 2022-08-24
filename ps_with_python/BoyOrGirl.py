str = input()
#distinct = [s for s in str if str.count(str[(str.index(s))]) <2]
#print(len(distinct))

str = list(dict.fromkeys(str))
if len(str)%2==0:
    print('CHAT WITH HER!')
else:
    print('IGNORE HIM!')

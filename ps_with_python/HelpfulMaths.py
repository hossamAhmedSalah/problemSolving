# she can calculate a sum only if the summands follow in non-decreasing order
str = input().split('+')

str = sorted(str)
for i in range(len(str)):
    if i == len(str)-1:
        print(str[i])
    else:
        print(str[i]+'+',end = '')

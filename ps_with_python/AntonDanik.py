numOfgames = int(input())
str = input()
D = str.count('D')
A = str.count('A')
if D>A:
    print('Danik')
elif A>D:
    print('Anton')
else:
    print('Friendship')

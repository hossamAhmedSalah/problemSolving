n, h = [int(x) for x in input().split()]
hOfFriends = [int(y) for y in input().split()]
widthSum = [1 if z <= h else 2 for z in hOfFriends]
print(sum(widthSum))

n = int(input())
cubes = [int(x) for x in input().split()]
#print(sorted(cubes))
for i in range(n):
    print(sorted(cubes)[i], end=' ')

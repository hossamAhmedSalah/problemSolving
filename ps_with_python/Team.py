n = int(input())
arr_main = []
for i in range(n):
    arr = [int(x) for x in input().split()]
    arr_main.append(arr)

numOfSolved = 0
for i in range(len(arr_main)):
    if arr_main[i].count(1) >=2:
        numOfSolved+=1
print(numOfSolved)

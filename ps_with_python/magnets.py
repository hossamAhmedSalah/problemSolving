n = int(input())
temp = 0
count = 1
for i in range(n):
   x = int(input())

   if x+temp == 11:
       count+=1

   temp = x


print(count)



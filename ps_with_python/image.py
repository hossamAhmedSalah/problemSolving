n = int(input())
pixels = []
e1,e2,e3,e4 = 0,0,0,0
E = []
output = []

temp = []
for i in range(n*2):
    pixel = input()
    temp.append(pixel)
    if not i%2 == 0:
     pixels.append(temp)
     temp = []

for i in range(len(pixels)):
    for j in range(1):

        output.append(pixels[i][0]+pixels[i][1])


for i in range(len(output)):
    E = []
    e1 = output[i].count(output[i][0])
    E.append(e1)
    e2 = output[i].count(output[i][1])
    E.append(e2)
    e3 = output[i].count(output[i][2])
    E.append(e3)
    e4 = output[i].count(output[i][3])
    E.append(e4)
    
    if E.count(4)==4:
        print(0)
        continue
    elif E.count(3)==3:
        print(1)
        continue
    elif E.count(2)==2:
        print(2)
        continue
    elif E.count(2)==4:
        print(1)
        continue
    elif E.count(1)==4:
        print(3)
        continue
'''
#the idea to know the distinct number of characters
set4 = {'a', 'a', 'a', 'a'}
set3 = {'a', 'a', 'a', 'b'}
set21 = {'a', 'a', 'b', 'b'}
set22 = {'a', 'a', 'b', 'c'}
set1 = {'a', 'b', 'c', 'd'}
print(len(set4)-1,
      len(set3)-1,
      len(set21)-1,
      len(set22)-1,
      len(set1)-1
      )
     #0 1 1 2 3
'''
'''
t=int(input())
for i in range(t):
    a=input()
    b=input()
    arr=[a[0],a[1],b[0],b[1]]
    print(len(set(arr))-1)
'''




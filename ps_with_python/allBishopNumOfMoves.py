from generateChessSquares import squares
#print(squares)
#c = input()
column = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
    "g": 7,
    "h": 8,
}

sim = []
for c in squares:
    frame0 = [4, 5]  # 13
    frame1 = [3, 6]  # 11
    frame2 = [2, 7]  # 9
    frame3 = [1, 8]  # 7

    if (column[c[0]] in frame3) or (int(c[1]) in frame3):
        #print(7, end=" ")
        sim.append(7)
    elif (column[c[0]] in frame2) or (int(c[1]) in frame2):
        #print(9, end=" ")
        sim.append(9)
    elif (column[c[0]] in frame1) or (int(c[1]) in frame1):
        #print(11, end=" ")
        sim.append(11)
    elif (column[c[0]] in frame0) or (int(c[1]) in frame0):
        #print(13, end=" ")
        sim.append(13)
for i in range(63,-1,-1):
    print(squares[i], end=" ")
    if i%8 == 0:
        print("\n")
print("\n")
print("#"*50)

for i in range(63,-1,-1):
    print(sim[i], end=" ")
    if i%8 == 0:
        print("\n")




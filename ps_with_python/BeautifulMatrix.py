matrix = []
mat_line = []
for i in range(5):
    mat_line = [int(c) for c in input().split()]
    #let's find the index when we take the input
    try:
        Row1 = mat_line.index(1)
        column1 = i
    except:
        continue
    matrix.append(mat_line)
# |Row1-2|+|column1-2|


print(abs(Row1-2)+abs(column1-2))

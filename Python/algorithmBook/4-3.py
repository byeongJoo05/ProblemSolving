data = input()

row = int(data[1])
column = int(ord(data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1,-2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0

for step in steps:
    nRow = row + step[0]
    nCol = column + step[1]

    if nRow >=1 and nRow<=8 and nCol>=1 and nCol<=8:
        result+=1

print(result)
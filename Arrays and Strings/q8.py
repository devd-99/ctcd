m = int(input())
n = int(input())
matrix = []
hmapX = {}
hmapY = {}
for i in range(m):
    
    t = []
    matrix.append(t)
    for j in range(n):
        tStr = str(i)+ ", " + str(j) + ": "
        matrix[i].append(int(input(tStr)))
print("\n\n")
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=", ")
    print()

for i in range(m):
    for j in range(n):
        if(matrix[i][j]==0):
            hmapX[i] = 1
            hmapY[j] = 1

for i in range(m):
    if(i in hmapX):
        for j in range(n):
            matrix[i][j]=0
    else:
        for j in range(n):
            if(j in hmapY):
                matrix[i][j]=0

print("\n\n")
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=", ")
    print()


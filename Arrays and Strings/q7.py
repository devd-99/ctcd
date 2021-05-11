m = int(input())
n = int(input())
matrix = []
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

for i in range(m-1):
    for j in range(i+1, n):
        temp = matrix[i][j]
        matrix[i][j] = matrix[j][i]
        matrix[j][i] = temp

print("\n\n")
for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=", ")
    print()
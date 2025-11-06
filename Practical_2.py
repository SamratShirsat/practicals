#Matrix Multiplication

A = [
 [1, 2, 3],
 [4, 5, 6]
]
B = [
 [7, 8],
 [9, 10],
 [11, 12]
]
result = [
 [0, 0],
 [0, 0]
]
for i in range(len(A)):
 for j in range(len(B[0])):
    for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]
print("Result of Matrix Multiplication:")
for row in result:
 print(row)

#Strassen Matrix Multiplication

def strassen(a, b):
 a11 = a[0][0]
 a12 = a[0][1]
 a21 = a[1][0]
 a22 = a[1][1]

 b11 = b[0][0]
 b12 = b[0][1]
 b21 = b[1][0]
 b22 = b[1][1]

 m1 = (a11 + a22) * (b11 + b22)
 m2 = (a21 + a22) * b11
 m3 = a11 * (b12 - b22)
 m4 = a22 * (b21 - b11)
 m5 = (a11 + a12) * b22
 m6 = (a21 - a11) * (b11 + b12)
 m7 = (a12 - a22) * (b21 + b22)
 c11 = m1 + m4 - m5 + m7
 c12 = m3 + m5
 c21 = m2 + m4
 c22 = m1 - m2 + m3 + m6
 return [[c11, c12],
         [c21, c22]]
A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]

result = strassen(A, B)
print("Result of Strassen Matrix Multiplication:")
for row in result:
 print(row)

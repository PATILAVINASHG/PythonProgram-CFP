
"""
   * Author - Avinash patil
   * Date -  23-01-2022
   * Time -  2.0PM
   * Title - 2DArray
"""

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))

twoDarray = []
print("Enter the entries rowwise:")

for i in range(R):
    a = []
    for j in range(C):
        a.append((input()))
    twoDarray.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(twoDarray[i][j], end=" ")
    print()
#Write a program to solve system of linear eqns using gauss elimination method

def gauss(matrix):
  n = len(matrix)                                                   #length of matrix as in rows

  for i in range(n):
    pivot = matrix[i][i]                                            #choosing pivot: 00, 11, 22...

    for j in range(n):
      if j != i:                                                    #avoiding the pivot elements
        eq = matrix[j][i] / pivot                                   # the equation to use for making the other elements 0
        for k in range(n+1):                                        # changing the elements along with the b vector
          matrix[j][k] -= eq * matrix[i][k]

    pivot = matrix[i][i]                                           # dividing pivot by itself so we get the solutions
    for j in range(n+1):
      matrix[i][j] /= pivot

matrix = [[2, 2, 1, 6],
         [4, 2, 3, 4],
         [1, 1, 1, 0]]

gauss(matrix)
    
for i in range(len(matrix)):
  print("x", i+1, "=", matrix[i][-1])

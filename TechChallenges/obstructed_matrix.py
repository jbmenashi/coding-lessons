# Number of paths in a 0-1 matrix

def uniquePathsWithObstacles(matrix):
   paths = [[0]*len(matrix[0] for i in A)]
   if matrix[0][0] == 0:
      paths[0][0] = 1

   for i in range(1, len(matrix)):
      if matrix[i][0] == 0:
         paths[i][0] = paths[i-1][0]

   for j in range(1, len(matrix[0])):
      if matrix[0][j] == 0:
         paths[0][j] = paths[0][j-1]

   for i in range(1, len[matrix]):
      for j in range(1, len(matrix[0])):
         if matrix[i][j] == 0:
            paths[i][j] = paths[i-1][j] + paths[i][j-1]
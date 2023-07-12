# 01 matrix

def updateMatrix(self, mat):

    if not mat:
     return mat

    rows = len(mat)
    cols = len(mat[0])
    dist = [[-1] * cols for _ in range(rows)]

    for i in range(rows):
       for j in range(cols):
          if mat[i][j] == 0:
             dist[i][j] ==0

          else: 
             dfs(mat, dist, i, j)

    return dist

def dfs(mat, dist, row, col):
   
   row = len(mat)
   col = len(mat[0])

   dr = [(0,1), (0,-1), (1,0), (-1,0)]

   for dx, dy in dr:
      newRow = dx+row
      newCol = dy+col

      if 0<newRow<row and 0<newCol<col:
        if not dist[newRow][newCol]:
                dist[newRow][newCol] = dist[row][col] + 1
                dfs(mat, dist, newRow, newCol)
        


    



#number of islands, DFS

def numIslands(grid):
    if not grid:
        return 0
    
    num_rows = len(grid)
    num_cols = len(grid[0])
    num_islands = 0

    def dfs(row, col):
        if row < 0 or col<0 and row >= num_rows or col >= num_cols or grid[row][col] == '0':
            return 
        
        grid[row][col] == '0'

        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)


    for i in range(num_rows):
        for j in range(num_cols):
            if grid[i][j] == '1':
                num_islands +=1

            dfs(i, j)
    return num_islands

        
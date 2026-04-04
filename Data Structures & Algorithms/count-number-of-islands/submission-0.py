class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        island = 0

        def isIsland(i, j):
            if i < 0 or i >= row or j < 0 or j >=col or grid[i][j] == "0":
                return
            grid[i][j] = "0"

            isIsland(i+1, j)
            isIsland(i-1, j)
            isIsland(i, j+1)
            isIsland(i, j-1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    island += 1
                    isIsland(i, j)
                
        return island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        max_area = 0

        def max_island_area(i, j):
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return (
                1 + 
                max_island_area(i, j+1) +
                max_island_area(i, j-1) +
                max_island_area(i+1, j) +
                max_island_area(i-1, j))
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    curr_max_area = max_island_area(i, j)
                    if curr_max_area > max_area:
                        max_area = curr_max_area

        return max_area

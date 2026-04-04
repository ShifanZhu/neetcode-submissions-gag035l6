class Solution:

    # def binarySearch(self, lst, target):
    #     left = 0
    #     right = len(lst) - 1
    #     while left <= right:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. get matrix size
        rows = len(matrix)
        cols = len(matrix[0])

        # boundary check
        if rows == 0 or cols == 0:
            return False

        # 2. iterate through first and last element of each row to find target row
        target_row = -1
        for i in range(rows):
            if matrix[i][0] <= target and matrix[i][cols-1] >= target:
                target_row = i
                break
        if target_row == -1:
            return False
        
        # 3. iterate target row to check (better with binary search)
        for j in range (cols):
            if matrix[target_row][j] == target:
                return True
        return False
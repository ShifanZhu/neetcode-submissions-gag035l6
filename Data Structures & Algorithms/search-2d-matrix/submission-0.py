class Solution:

    # def binarySearch(self, lst, target):
    #     left = 0
    #     right = len(lst) - 1

    #     while left <= right:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 1. get matrix size
        rows = len(matrix)
        cols = len(matrix[0])
        # print("row col ", rows, cols)

        for i in range(rows):
            # 2. iterate through first element of each row to find target row
            if matrix[i][0] < target:
                continue
            print("i: ", i)
            # 3. iterate target row to check (better with binary search)
            j = 0
            while j < cols:
                print("j: ", j)
                if matrix[i-1][j] == target:
                    return True
                j += 1
        return False


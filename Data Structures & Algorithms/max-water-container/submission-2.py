class Solution:

    # Brute Force
    # def maxArea(self, heights: List[int]) -> int:
    #     heights_len = len(heights)
    #     print("len: ", heights_len)

    #     max_area = 0
    #     for i in range(heights_len):
    #         for j in range(i+1, heights_len):
    #             area = min(heights[i], heights[j]) * (j - i)
    #             if area > max_area:
    #                 max_area = area
        
    #     return max_area

    def maxArea(self, heights: List[int]) -> int:
        heights_len = len(heights)

        left = 0
        right = heights_len - 1

        max_area = 0
        while left < right:
            area = min(heights[left], heights[right]) * (right - left)
            if area > max_area:
                max_area = area
            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left += 1
            else:
                right -=1 
        return max_area

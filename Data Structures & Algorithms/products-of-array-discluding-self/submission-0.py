class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        
        # left products
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        
        # right products
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res

# nums = [1,2,4,6]
# after left products: res = [1, 1, 2, 8]
# after right products: [, 8]
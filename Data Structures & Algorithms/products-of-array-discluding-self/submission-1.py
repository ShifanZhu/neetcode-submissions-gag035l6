class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        print("nums: ", nums)
        
        # left products
        left = 1
        for i in range(n):
            res[i] = left
            left *= nums[i]
        print("left: ", left)
        print("res: ", res)
        
        # right products
        right = 1
        for i in range(n - 1, -1, -1):
            res[i] *= right
            right *= nums[i]
        print("right: ", right)
        print("res: ", res)

        return res

# nums = [1,2,4,6]
# after left products: res = [1, 1, 2, 8]
# after right products: [48, 24, 12, 8]
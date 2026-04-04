class Solution:

    # Does not work

    # def twoSum(self, nums: List[int], target):
    #     left = 0
    #     right = len(nums) - 1
    #     nums = sorted(nums)
    #     while left < right:
    #         sum = nums[left] + nums[right]
    #         if sum == target:
    #             return [nums[left], nums[right]]
    #         elif sum > target:
    #             right -= 1
    #         else:
    #             left += 1
    #     return []

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     results = []

    #     print("nums: ", nums)

    #     nums = sorted(nums)
    #     print("sorted nums: ", nums)
    #     for i, num in enumerate(nums):
    #         target = -num
    #         two_sum_return = self.twoSum(nums, target)

    #         if len(two_sum_return) == 2:
    #             result = [two_sum_return[0], two_sum_return[1], num]
    #             results.append(result)

    #     return results


    # Solution 1

    # def twoSum(self, nums: List[int], start: int, target: int) -> List[List[int]]:
    #     left = start
    #     right = len(nums) - 1
    #     pairs = []

    #     while left < right:
    #         current_sum = nums[left] + nums[right]

    #         if current_sum == target:
    #             pairs.append([nums[left], nums[right]])
    #             left += 1
    #             right -= 1

    #             while left < right and nums[left] == nums[left - 1]:
    #                 left += 1

    #             while left < right and nums[right] == nums[right + 1]:
    #                 right -= 1
    #         elif current_sum > target:
    #             right -= 1
    #         else:
    #             left += 1

    #     return pairs

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     results = []
    #     nums.sort()

    #     for i, num in enumerate(nums):
    #         if i > 0 and num == nums[i - 1]:
    #             continue

    #         target = -num
    #         two_sum_results = self.twoSum(nums, i + 1, target)

    #         for pair in two_sum_results:
    #             results.append([num, pair[0], pair[1]])

    #     return results

    # Solution 2

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     nums.sort()
    #     results = []

    #     for i, num in enumerate(nums):
    #         if i > 0 and num == nums[i - 1]:
    #             continue

    #         left = i + 1
    #         right = len(nums) - 1

    #         while left < right:
    #             total = num + nums[left] + nums[right]

    #             if total == 0:
    #                 results.append([num, nums[left], nums[right]])
    #                 left += 1
    #                 right -= 1

    #                 while left < right and nums[left] == nums[left - 1]:
    #                     left += 1

    #                 while left < right and nums[right] == nums[right + 1]:
    #                     right -= 1
    #             elif total < 0:
    #                 left += 1
    #             else:
    #                 right -= 1

    #     return results

    # Solution 3:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    res.add((nums[i], nums[left], nums[right]))  # tuple for set
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return [list(t) for t in res]
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Solution 1: works but O(n^2)
        # result = []

        # for i, t in enumerate(temperatures):
        #     sub_temp = temperatures[i:]
        #     larger_mask = [1 if st > t else 0 for st in sub_temp]
        #     first_larger_idx = larger_mask.index(1) if 1 in larger_mask else 0
        #     result.append(first_larger_idx)

        # return result

        # Solution 2:
        result = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # if current temperature is warmer than unsolved days in stack
            while stack and t > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
                print("i idx: ", i, idx)
            stack.append(i)
            print("i, stack: ", i, stack)

        return result
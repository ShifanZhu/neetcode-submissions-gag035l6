class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_sub_str = 0
        left = 0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[i])
            max_sub_str = max(max_sub_str, i - left + 1)
        return max_sub_str


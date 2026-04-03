from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return set(s) == set(t)
        return Counter(s) == Counter(t)
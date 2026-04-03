from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return set(s) == set(t) # does not work for 'xx' and 'x'
        # return Counter(s) == Counter(t) # works
        return sorted(s) == sorted(t)
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            # print("sorted(s): ", sorted(s))
            # print("str(sorted(s)): ", str(sorted(s)))
            key = ''.join(sorted(s))
            groups[key].append(s)

        return list(groups.values())
# import queue
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        # Solution 1, works but not clean
        # seen = deque()
        # valid = False
        # for c in s:
        #     if c in '[({':
        #         seen.append(c)
        #     elif c in '])}':
        #         if not seen:
        #             return False
        #         if c == ']':
        #             valid = (seen.pop() == '[')
        #             if not valid:
        #                 return False
        #         if c == ')':
        #             valid = (seen.pop() == '(')
        #             if not valid:
        #                 return False
        #         if c == '}':
        #             valid = (seen.pop() == '{')
        #             if not valid:
        #                 return False
        # return len(seen) == 0

        # Solution 2
        seen = deque()
        pair = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for c in s:
            if c in pair.values():
                seen.append(c)
            else: # keys
              if pair[c] != seen.pop() and not pair:
                return False
        return len(seen) == 0
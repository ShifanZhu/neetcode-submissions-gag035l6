# import queue
from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        seen = deque()
        valid = False
        for c in s:
            if c in '[({':
                # print("c is: ", c)
                seen.append(c)
            if c in '])}':
                if c == ']':
                    valid = (seen.pop() == '[')
                    # print("valid: ", valid)
                    if not valid:
                        return False
                if c == ')':
                    valid = (seen.pop() == '(')
                    # print("valid: ", valid)
                    if not valid:
                        return False
                if c == '}':
                    valid = (seen.pop() == '{')
                    # print("valid: ", valid)
                    if not valid:
                        return False
        return True
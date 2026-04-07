from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_time = max(piles)
        speed = 0
        for s in range(1, max_time+1):
            accumulated_time = 0
            for p in piles:
                accumulated_time += ceil(p / s)
            if accumulated_time <= h:
                return s
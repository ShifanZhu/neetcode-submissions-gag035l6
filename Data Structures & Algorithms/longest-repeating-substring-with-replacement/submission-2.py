class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        # r = len(s) - 1
        max_len = 0
        max_freq = 0
        freq = defaultdict(int)

        for r, c in enumerate(s):
            freq[c] += 1
            max_freq = max(max_freq, freq[c])

            while r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            max_len = max(max_len, r - l + 1)

        return max_len
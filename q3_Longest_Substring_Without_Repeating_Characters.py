class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        bar = set()
        right = 0
        result = 0

        for left in range(n):
            while right < n and s[right] not in bar:
                bar.add(s[right])
                result = max(result, right-left+1)
                right += 1
            bar.remove(s[left])

        return result

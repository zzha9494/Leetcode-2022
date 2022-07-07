class Solution:
    def romanToInt(self, s: str) -> int:
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = 0
        i = 0
        while i < len(s):
            if i != len(s) - 1 and s[i] + s[i+1] in symbols:
                res += nums[symbols.index(s[i] + s[i+1])]
                i += 2
            else:
                res += nums[symbols.index(s[i])]
                i += 1
        return res

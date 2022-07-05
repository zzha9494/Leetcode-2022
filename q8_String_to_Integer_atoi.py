class Solution:
    def myAtoi(self, s: str) -> int:
        MIN = -2 ** 31
        MAX = 2**31 - 1
        num = [str(_) for _ in range(10)]
        minus = False
        s = s.strip()

        if len(s) == 0:
            return 0

        if s[0] == '-' or s[0] == '+':
            minus = s[0] == '-'
            s = s[1:]

        if len(s) == 0 or s[0] not in num:
            return 0

        i = 0
        while i < len(s):
            if s[i] not in num:
                s = s[:i]
                break
            i += 1

        s = int(s)

        if minus:
            s = -s

        if s < MIN:
            return MIN
        if s > MAX:
            return MAX
        return s

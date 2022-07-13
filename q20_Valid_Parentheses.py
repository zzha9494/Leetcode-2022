class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        a = ['(', ')', '{', '}', '[', ']']

        for i in range(len(s)):
            if s[i] in a[::2]:
                stack.append(s[i])
            elif not stack and s[i] in a[1::2]:
                return False
            else:
                if s[i] == a[1] and stack[-1] != a[0]:
                    return False
                if s[i] == a[3] and stack[-1] != a[2]:
                    return False
                if s[i] == a[5] and stack[-1] != a[4]:
                    return False
                stack.pop()
        return len(stack) == 0

    # leetcode
    def isValid1(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        pairs = {
            ")": "(",
            "]": "[",
            "}": "{",
        }
        stack = list()
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        temp = ["" for _ in range(numRows)]

        for i in range(len(s)):
            x = i % (2 * numRows - 2)

            if x <= numRows - 1:
                temp[x] += s[i]
            else:
                x = x - numRows + 1
                temp[numRows - 1 - x] += s[i]

        result = ''
        for i in temp:
            result += i
        return result

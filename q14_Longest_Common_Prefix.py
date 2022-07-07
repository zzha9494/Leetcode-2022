from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a = set()
        index = 0

        try:
            while True:
                for string in strs:
                    a.add(string[index])
                if len(a) != 1:
                    break
                a.clear()
                index += 1
        except IndexError:
            pass
        return strs[0][:index]

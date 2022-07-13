from functools import lru_cache
from typing import List


class Solution:
    @lru_cache()
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return [""]

        ans = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n-1-i):
                    ans.append(f"({left}){right}")
        return ans

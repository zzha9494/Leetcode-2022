from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        dic = {'2': 'abc',
               '3': 'def',
               '4': 'ghi',
               '5': 'jkl',
               '6': 'mno',
               '7': 'pqrs',
               '8': 'tuv',
               '9': 'wxyz'}

        def helper(current_digits, current_result: str):
            if len(current_digits) == 0:
                ans.append(current_result)
            else:
                for char in dic[current_digits[0]]:
                    helper(current_digits[1:], current_result + char)

        ans = []
        helper(digits, "")
        return ans

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = -1, len(nums)
        if r == 0:
            return [-1, -1]

        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m
            else:
                r = m

        ans = []
        if r == len(nums) or nums[r] != target:
            return [-1, -1]
        else:
            ans.append(r)

        l, r = -1, len(nums)
        while l + 1 != r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m
            else:
                r = m

        ans.append(l)
        return ans

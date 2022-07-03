from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """one for loop traversal, and check if the remainder of subtraction is in the remaining list."""
        for i in range(0, len(nums)):
            if target - nums[i] in nums[i + 1:]:
                return [i, nums.index(target-nums[i], i+1)]

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """Hash and dictionary, key is the number and value is the index."""
        a = {}
        for index, item in enumerate(nums):
            if target - item in a.keys():
                return [index, a[target - item]]
            a[item] = index

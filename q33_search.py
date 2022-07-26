from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        return self.helper(0, len(nums) - 1, nums, target)

    def helper(self, left, right, nums, target):
        if left == right:
            if nums[left] == target:
                return left
            else:
                return -1

        if target == nums[left]:
            return left
        if target == nums[right]:
            return right

        mid = (left + right) // 2
        if nums[mid] == target:
            return mid

        if nums[left] < nums[mid]:
            if nums[left] < target < nums[mid]:
                return self.helper(left, mid, nums, target)
            else:
                return self.helper(mid + 1, right, nums, target)
        else:
            if nums[mid] < target < nums[right]:
                return self.helper(mid + 1, right, nums, target)
            else:
                return self.helper(left, mid, nums, target)
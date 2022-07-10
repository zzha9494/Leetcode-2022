from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        ans = sum(nums[:3])

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1
            current_max = nums[i] + nums[right - 1] + nums[right]
            current_min = nums[i] + nums[left] + nums[left + 1]

            if current_max <= target:
                if abs(target - current_max) < abs(target - ans):
                    ans = current_max
                    if ans == target:
                        return ans
                continue

            if current_min >= target:
                if abs(target - current_min) < abs(target - ans):
                    ans = current_min
                break  # current_min 只会变大 因为i增大

            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return temp
                elif abs(target - temp) < abs(target - ans):
                    ans = temp

                if temp > target:
                    right -= 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                else:
                    left += 1
                    while left < right and nums[left - 1] == nums[left]:
                        left += 1

        return ans

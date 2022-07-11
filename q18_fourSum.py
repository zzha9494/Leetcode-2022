from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)

        if n < 4:
            return []

        ans = []
        nums.sort()

        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            max = nums[i] + nums[-3] + nums[-2] + nums[-1]
            min = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if max < target:
                continue
            if min > target:
                break

            for j in range(i + 1, n-2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                max = nums[i] + nums[j] + nums[-2] + nums[-1]
                min = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if max < target:
                    continue
                if min > target:
                    break

                start, end = j + 1, n - 1
                while start < end:
                    result = nums[i] + nums[j] + nums[start] + nums[end]
                    if result == target:
                        ans.append([nums[i], nums[j], nums[start], nums[end]])

                    if result <= target:
                        start += 1
                        while start < end and nums[start] == nums[start - 1]:
                            start += 1

                    if result >= target:
                        end -= 1
                        while start < end and nums[end] == nums[end + 1]:
                            end -= 1
        return ans

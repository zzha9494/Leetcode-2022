from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []

        nums.sort()
        res = []

        index = 0
        while index < len(nums):
            if index != 0 and nums[index] == nums[index - 1]:
                index += 1
                continue

            start, end = index + 1, len(nums) - 1
            while start < end:
                sum = nums[start] + nums[end]

                if sum == -nums[index]:
                    temp = [nums[index], nums[start], nums[end]]
                    res.append(temp)
                    start += 1
                    end -= 1
                    if len(res) > 1 and res[-1] == res[-2]:
                        res.remove(temp)
                elif sum > -nums[index]:
                    end -= 1
                else:
                    start += 1
            index += 1
        return res

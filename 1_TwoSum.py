from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()

        for i in range(len(nums)):
            expect_num = target - nums[i]
            if expect_num in d:
                return [d.get(expect_num), i]
            else:
                d[nums[i]] = i

        return []
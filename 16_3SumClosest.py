from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)

        mn = sum(nums[:3])
        for j in range(len(nums) - 2):
            i = j + 1
            k = n - 1
            while i < k:
                sm = nums[i] + nums[j] + nums[k]
                mn = min(mn, sm, key = lambda x: abs(target - x))
                if sm < target:
                    i += 1
                else:
                    k -= 1
        return mn
            
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)

        res = dict()
        for i in range(n - 2):
            j = i + 1
            k = n - 1
            while j < k:
                curr = nums[i] + nums[j] + nums[k]
                if curr == 0 and (m := (nums[i], nums[j], nums[k])) not in res:
                    res[m] = True
                if curr < 0:
                    j += 1
                else:
                    k -= 1
        return [[*key] for key in res.keys()]
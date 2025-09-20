from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 1:
            return nums[0]
        prefix, max_pref_sum = self.prefix_sum(nums, size)
        min_pref_sum = 0
        for i in range(size):
            max_pref_sum = max(prefix[i] - min_pref_sum, max_pref_sum)
            min_pref_sum = min(prefix[i], min_pref_sum)
        return max_pref_sum


    def prefix_sum(self, arr: List[int], size: int) -> (List[int], int):
        pref_sum = [0] * size
        pref_sum[0] = arr[0]
        max_sum = arr[0]
        for i in range(1, size):
            pref_sum[i] = pref_sum[i-1] + arr[i]
            max_sum = max(pref_sum[i], max_sum)
        return pref_sum, max_sum
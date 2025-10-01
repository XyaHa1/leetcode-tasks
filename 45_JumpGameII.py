class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('inf')] * n
        dp[0] = 0

        max_search = 0
        for i in range(n - 1):
            if i > max_search:
                continue

            max_search = max(i + nums[i], max_search)
            for j in range(min(n - 1, max_search), i, -1):
                dp[j] = min(dp[j], dp[i] + 1)

                if j == n - 1:
                    return dp[j]

        return dp[-1]
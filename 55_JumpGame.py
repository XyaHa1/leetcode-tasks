class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        
        max_jump = 0
        for i in range(n - 1):
            if i > max_jump or nums[i] == 0:
                continue

            max_jump = max(max_jump, i + nums[i])
            if min(max_jump, n - 1) == n - 1:
                return True

        return False
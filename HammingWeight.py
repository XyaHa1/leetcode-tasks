class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while count <= n:
            n &= n - 1
            count += 1
        return count

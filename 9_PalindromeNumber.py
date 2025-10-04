class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        new_num = 0
        curr = x
        while curr > 0:
            new_num = new_num * 10 + curr % 10
            curr //= 10

        return x == new_num

class Solution:
    def isBits64(self, n: int) -> bool:
        if n >= 0:
            return (n >> 31) == 0

        return (n >> 31) == -1

    def reverse(self, x: int) -> int:
        if not self.isBits64(x):
            return 0

        sign = (-1) ** (x < 0)

        x = abs(x)
        rev_int = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if not self.isBits64(rev_int):
                return 0
            rev_int = rev_int * 10 + digit

        rev_int *= sign
        if not self.isBits64(rev_int):
            return 0
        return rev_int

class Solution:
    def int32(self, n: int) -> int:
        """
        If n < 0: r = -1
        else: r = 0
        """
        return n >> 31


    def divide(self, dividend: int, divisor: int) -> int:
        quotient = 0

        sign = (-1) ** (dividend < 0) * (-1) ** (divisor < 0)
        divisor = abs(divisor)
        dividend = abs(dividend)
        quotient = 0
        temp = 0
        for i in range(31, -1, -1):
            if temp + (divisor << i) <= dividend:
                temp += divisor << i
                quotient |= 1 << i

        quotient *= sign
        isInt32 = self.int32(quotient)
        if isInt32 > 0:
            return 2 ** 31 - 1
        if isInt32 < -1:
            return - 2 ** 31
        return quotient

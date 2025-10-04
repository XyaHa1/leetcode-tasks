class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        if s[0] in ('-', '+'):
            if s[0] == '-':
                sign = -1
            s = s[1:]

        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)

        result *= sign
        INT_MAX = 2 ** 31 - 1
        INT_MIN = - 2 ** 31

        if result > INT_MAX:
            return INT_MAX
        if result < INT_MIN:
            return INT_MIN

        return result

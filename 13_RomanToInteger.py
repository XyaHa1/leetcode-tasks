class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) == 0 or len(s) > 15:
            ValueError()

        arabic_romes = [(1000, 'M'), (900, 'CM'), (500, 'D'),
                (400, 'CD'), (100, 'C'), (90, 'XC'),
                (50, 'L'), (40, 'XL'), (10, 'X'),
                (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
        result = 0
        for arabic, rome in arabic_romes:
            while s.startswith(rome):
                result += arabic
                s = s[len(rome):]

            if len(s) == 0:
                return result

        return result
        
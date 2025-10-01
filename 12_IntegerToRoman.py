class Solution:
    def intToRoman(self, num: int) -> str:
        arabic_romes = [(1000, 'M'), (900, 'CM'), (500, 'D'),
                        (400, 'CD'), (100, 'C'), (90, 'XC'),
                        (50, 'L'), (40, 'XL'), (10, 'X'),
                        (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

        if num < 1 or num > 3999:
            ValueError(f'Expected number > 0, got {number}')

        result: List[str] = []
        for arabic, rome in arabic_romes:
            if num >= arabic:
                count = num // arabic
                num %= arabic
                result += rome * count

        return ''.join(result)

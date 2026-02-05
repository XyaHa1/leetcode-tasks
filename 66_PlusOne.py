from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)
        while (i := i - 1) >= 0:
            plus = (digits[i] + 1) // 10
            digits[i] = (digits[i] + 1) % 10
            if plus == 0:
                break
            if i == 0:
                digits = [1] + digits
        return digits
    

if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([9, 9, 9]))
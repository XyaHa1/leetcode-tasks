from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        out = []
        for i in range(2 ** n):
            out.append(i ^ (i >> 1))
        return out
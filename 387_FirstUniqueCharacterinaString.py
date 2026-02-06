class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i, l in enumerate(s):
            if l in d:
                d[l] = (d.get(l)[0], d.get(l)[1] + 1)
            else:
                d[l] = (i, 1)
        return min([d[l][0] for l in d if d[l][1] == 1] or [-1])
    
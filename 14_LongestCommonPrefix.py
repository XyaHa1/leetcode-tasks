class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = {}
        for word in strs:
            for i in range(len(word)):
                pref = word[0:i + 1]
                prefix[pref] = prefix.get(pref, 0) + 1

        res = self.maxPref(prefix, len(strs))

        return res

    def maxPref(self, prefix: dict[str, int], words_count: int) -> str:
        result = ""
        for pref, count in prefix.items():
            if count == words_count and len(pref) > len(result):
                result = pref
        return result


if __name__ == '__main__':
    class Test:
        sol = Solution()
        assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
        assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""
        assert sol.longestCommonPrefix(["ab", "a"]) == "a"
        assert  sol.longestCommonPrefix(["a"]) == "a"
        assert sol.longestCommonPrefix(['number', 'numbers', 'numbered']) == 'number'
        assert sol.longestCommonPrefix(['cat', 'car', 'cattle']) == 'ca'
        assert sol.longestCommonPrefix(['cat', 'car', 'cattle', 'cat', 'car', 'cattle']) == 'ca'
        assert sol.longestCommonPrefix(["",""]) == ""
        assert sol.longestCommonPrefix(["cir","car"]) == "c"
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s) - 1
        while i >= 0:
            if s[i] == ' ':
                i -= 1
            elif s[i].isalpha():
                while i >= 0 and s[i].isalpha():
                    i -= 1
                return len(s) - i - 1
        return 0

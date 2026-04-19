from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):return False
        c_s = Counter(s)
        c_t = Counter(t)

        for ch in s:
            if c_s[ch] != c_t[ch]:
                return False
        return True
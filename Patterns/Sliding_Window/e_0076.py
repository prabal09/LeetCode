from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        need_cnt = len(need)          # distinct chars still to satisfy
        have = 0                       # distinct chars currently satisfied
        window = {}
        best_len, best = float("inf"), (0, 0)
        left = 0

        for right, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1

            while have == need_cnt:            # window is valid -> shrink
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best = (left, right)
                lch = s[left]
                window[lch] -= 1
                if lch in need and window[lch] < need[lch]:
                    have -= 1
                left += 1

        l, r = best
        return s[l:r+1] if best_len != float("inf") else ""

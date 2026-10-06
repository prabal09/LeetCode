from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        need_cnt = len(need)                    # distinct chars needed to satisfy
        have = 0                                # distinct chars currently satisfied
        window = {}                             # Counts of characters in the active substring
        best_len, best = float("inf"), (0, 0)   # Tracks the length and (left, right) indices of the smallest valid window seen so far
        left = 0

        for right, ch in enumerate(s):
            #expand the window - start
            window[ch] = window.get(ch, 0) + 1
            if ch in need and window[ch] == need[ch]:
                have += 1                       # have Increments by 1 only when a character's current frequency in the window reaches its required amount
            #expand the window - end

            # window is valid -> shrink
            while have == need_cnt:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best = (left, right)
                lch = s[left]
                window[lch] -= 1
                if lch in need and window[lch] < need[lch]:
                    have -= 1
                left += 1                       # shrinking by moving left

        l, r = best
        return s[l:r+1] if best_len != float("inf") else ""

'''
Time: O(|s| + |t|)
Space: O(|s| + |t|)
'''

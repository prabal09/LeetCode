class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_length = 0
        max_freq = 0
        left = 0

        for right,ch in enumerate(s):
            # Add the incoming character to our frequency map
            count[ch] = count.get(ch, 0) + 1

            # Update the peak frequency seen in the current window structure
            max_freq = max(max_freq, count[ch])

            # If the current window size minus max_freq exceeds k, it's invalid
            window_len = right - left + 1
            if window_len - max_freq > k:
                # Shrink the window from the left
                count[s[left]] -= 1
                left += 1

            # Recalculate window length after potential adjustment
            max_length = max(max_length, right - left + 1)

        return max_length

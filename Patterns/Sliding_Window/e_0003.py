class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # maps character -> its last seen index
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            # If the character is in the current window, jump the left pointer
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
                
            char_map[char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length

## O(n), O(min(m,n)) or O(1) assuming only a-z (26 letters)
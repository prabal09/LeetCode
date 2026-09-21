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
'''
seen, L, best on "abcabcbb":
R=0 a  char_map{a-0}       L=0  best=1
R=1 b  char_map{a-0,b-1}     L=0  best=2
R=2 c  char_map{a-0,b-1,c-2}   L=0  best=3
R=3 a  'a' in char_map → drop s[0]=a, L=1 → char_map{b-1,c-2}; add a → {b,c,a}  best=3
R=4 b  'b' in char_map → drop s[1]=b, L=2 → {c-2,a-3}; add b → {c,a,b}      best=3
R=5 c  'c' in char_map → drop s[2]=c, L=3 → {a-3,b-3}; add c → {a,b,c}      best=3
R=6 b  drop a(L=4), drop b(L=5) → {c}; add b → {c,b}               best=3
R=7 b  drop c(L=6), drop b(L=7) → {}; add b → {b}                  best=3
                                                          answer → 3
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1

            seen.add(s[right])
            max_length = max(max_length,right - left + 1)

        return max_length

'''
seen, L, best on "abcabcbb":
R=0 a  seen{a}       L=0  best=1
R=1 b  seen{a,b}     L=0  best=2
R=2 c  seen{a,b,c}   L=0  best=3
R=3 a  'a' in seen → drop s[0]=a, L=1 → seen{b,c}; add a → {b,c,a}  best=3
R=4 b  'b' in seen → drop s[1]=b, L=2 → {c,a}; add b → {c,a,b}      best=3
R=5 c  'c' in seen → drop s[2]=c, L=3 → {a,b}; add c → {a,b,c}      best=3
R=6 b  drop a(L=4), drop b(L=5) → {c}; add b → {c,b}               best=3
R=7 b  drop c(L=6), drop b(L=7) → {}; add b → {b}                  best=3
                                                          answer → 3
'''

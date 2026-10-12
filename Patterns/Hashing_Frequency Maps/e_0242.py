class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        check_list = [0]*26
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            str_s = s[i];
            str_t = t[i]
            check_list[ord(str_s) - ord('a')] +=1
            check_list[ord(str_t) - ord('a')] -=1

        return all(count == 0 for count in check_list)

'''
Time Complexity: (O(n)
Space Complexity: O(1), since the list always contains 26 elements.
'''

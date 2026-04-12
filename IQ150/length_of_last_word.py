class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end_idx = len(s)-1
        while s[end_idx] == " ":
            end_idx -=1

        count = 0
        for i in range(len(s[:end_idx+1])):
            if s[i] == " ":
                count = 0
            else:
                count +=1
        return count
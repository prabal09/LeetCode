class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = str(x)
        len_y = len(y)
        return all([y[i] == y[len_y-i-1] for i in range(len_y)])

import math
class Solution1:
    def climbStairs(self, n: int) -> int:
        terms = (n-1)//2
        addons = 1 if n%2 == 1 else 2
        for i in range(terms):
            addons += int(factorial(n-i-1)/(factorial(n-2*i-2)*factorial(i+1)))
        return addons

class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        prev_n_1 = 1;
        prev_n_2 = 2;

        for _ in range(n-2):
            curr = prev_n_1 + prev_n_2
            prev_n_1 = prev_n_2
            prev_n_2 = curr

        return prev_n_2

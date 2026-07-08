class Solution0:
    def hammingWeight(self, n: int) -> int:
        n_b = bin(n)[2:]
        count = 0
        for c in n_b:
            if c == '1':
                count += 1
        return count

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            count += (n & 1)
            n = n >> 1
        return count

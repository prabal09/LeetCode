class Solution1:
    def reverseBits(self, n: int) -> int:
        n_b = bin(n)[2:]
        n_b = n_b[::-1]
        n_b = n_b + '0'*(32-len(n_b))
        return int(n_b,2)

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n = n >> 1
        return res

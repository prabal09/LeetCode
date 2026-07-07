class Solution:
    def trailingZeroes(self, n: int) -> int:
        summ = 0
        five = 5
        while int(n/five) !=0:
            summ += floor(n/five)
            five = five*5
            print(summ,five)
        return summ

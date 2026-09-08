class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total_drunk = numBottles
        empty_bottles = numBottles
        while empty_bottles >= numExchange:
            new_full = empty_bottles // numExchange
            total_drunk += new_full

            empty_bottles = (empty_bottles % numExchange) + new_full
        return total_drunk

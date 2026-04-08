class Solution1:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0; sell = 1
        maxP = 0
        # print(buy,sell,maxP)
        while sell<len(prices):
            if prices[sell] - prices[buy]>maxP:
                maxP = prices[sell] - prices[buy]
            if prices[sell]<prices[buy]:
                buy = sell
            sell +=1
            # print(buy,sell,maxP)
        return maxP
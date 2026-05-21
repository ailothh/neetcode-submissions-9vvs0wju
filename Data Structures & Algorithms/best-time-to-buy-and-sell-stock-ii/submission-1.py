class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for num in range(1,len(prices)):
            if prices[num]>prices[num-1]:
                profit += prices[num]-prices[num-1]
        return profit

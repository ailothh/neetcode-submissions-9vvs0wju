class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxcount=0
        total=0
        for num1 in range(len(prices)):
            for num2 in range(num1+1, len(prices)):
                total=prices[num2]-prices[num1]
                maxcount=max(maxcount,total)
        return maxcount

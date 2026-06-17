class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        profit = 0
        min_buy_so_far = prices[0]
        for i in range(len(prices)):
            
            # calculate the profit
            profit = prices[i] - min_buy_so_far
            
            # Update the max profit 
            max_profit = max(max_profit,profit)

            # Update the min so far 
            min_buy_so_far = min(min_buy_so_far,prices[i])
        
        return max_profit
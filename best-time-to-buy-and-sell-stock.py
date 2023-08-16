class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        # Set buy to first element in prices list
        buy=prices[0]
        profit=0
        # Loop through the rest of prices list
        for price in prices[1:]:
        	# Check current price in loop with buy price
            if price > buy:
            	# Set profit to max of old profit and new profit ( price - buy )
                profit=max(profit, price - buy)
            else:
            	# Set buy to price
                buy=price
        return profit


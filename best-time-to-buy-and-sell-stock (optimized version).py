def maxProfit(prices: list[int]) -> int:
    count=0
    buy_price=0
    sell_price=0
    profit=0
    # Loop through prices list
    for b_price in prices:
        count+=1
        # Check if cutted list isn't empty
        if (len(prices[count:])!= 0):
        	# Get max value in cutted prices list
            s_price=max(prices[count:])
            # Check if sell price greater than buy price 
            if s_price > b_price:
            	# Compute buy sell profit price
                bs_profit = s_price - b_price
                # Check saved profit with new computed profit
                if bs_profit > profit:
                    # Set profit to new profit and also with buy_price and sell_price
                    profit=bs_profit
                    buy_price=b_price
                    sell_price=s_price
    return profit


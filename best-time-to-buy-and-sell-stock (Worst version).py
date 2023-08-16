def maxProfit(prices: list[int]) -> int:
    count=0
    buy_price=0
    sell_price=0
    profit=0
    for b_price in prices:
        count+=1
        for s_price in prices[count:]:
            if s_price > b_price:
                bs_profit = s_price - b_price
                if bs_profit > profit:
                    profit=bs_profit
                    buy_price=b_price
                    sell_price=s_price
    return profit


class Solution(object):
    def maxProfit(self, prices):
        min_ele = prices[0]
        max_profit = 0

        for price in prices:
            min_ele = min(min_ele, price)
            max_profit = max(max_profit, price - min_ele)

        return max_profit
class Solution(object):
    def maxProfit(self, prices):
        min_ele = max(prices)
        max_profit = 0
        for i in prices:
            min_ele = min(min_ele,i)
            max_profit = max(max_profit,i-min_ele)

        return max_profit
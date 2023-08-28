from typing import List


# We might think about using sliding window technique, but obviously we don't need subarray here.
# We just need one value from the given input list. So, this technique is not useful.
# We always need to know what is the maxProfit we can make if we sell the stock on i-th day.
# So, keep track of maxProfit.
# There might be a scenario where if stock bought on i-th day is minimum and we sell it on (i + k)th day.
# So, keep track of minPurchase as well.

class Solution:
    @staticmethod
    def max_profit(prices: List[int]) -> int:
        max_profit = 0
        min_purchase = prices[0]

        for price in prices:
            cur_profit = price - min_purchase
            if cur_profit > max_profit:
                max_profit = cur_profit
            if price < min_purchase:
                min_purchase = price
        return max_profit


prices = [7, 1, 5, 3, 6, 4]
expected = 5
assert Solution().max_profit(prices) == 5
print("OK")

from typing import List


class Solution:
    # Bottom-Up DP (cache and use min amount of coins from 0 to N)
    # Calculate how much coins we need to get every N from amount
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialize DP memoization array to store min coins
        # for each amount from 0 to N
        dp = [amount + 1] * (amount + 1)
        # To get amount=0 we need 0 coins -> initialize first DP element
        dp[0] = 0

        # iterate over all possibble values from 1 to N (amount)
        for n in range(1, amount + 1):
            # iterate over each coin in coins
            for coin in coins:
                # we have options to get amount only if amount >= current coin
                if n - coin >= 0:
                    # taking min from current value(MAX) and 1 coin + memo of the rest
                    dp[n] = min(dp[n], 1 + dp[n - coin])
        # return only if final amount (N) was updated otherwise no solution (-1)
        return dp[amount] if dp[amount] != amount + 1 else -1

coins = [1,3,4,5]
amount = 7
assert Solution().coinChange(coins, amount) == 2
print("OK")

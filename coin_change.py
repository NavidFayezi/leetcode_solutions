class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sorted_coins = sorted(coins)
        no_coins = len(coins)
        dp_table = [0] + [(amount + 1) for k in range(amount)]

        for i in range(1, no_coins + 1):
            current_coin = sorted_coins[i -1]
            for j in range(current_coin, amount + 1):
                cost_of_including_j = 1 + dp_table[j - current_coin]
                dp_table[j] = min(dp_table[j]
                                    ,cost_of_including_j)
 
        if dp_table[amount] == (amount + 1):
            rv = -1
        else:
            rv = dp_table[amount]
        return rv
        
class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        # initialize ways[0] to 1 and set the rest of the array to zero
        ways = [1] + [0]*amount
        for coin in coins:
            for current_amount in range(amount+1):
                if current_amount-coin >= 0:
                    ways[current_amount] += ways[current_amount-coin]
        return ways[amount]
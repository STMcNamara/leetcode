from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
                     
        memo = {}
        
        def recurse(rem):
            """
            Returns the min num of coins to clear rem
            """
            # base case - remaining amount is zero
            if rem == 0:
                return rem
            # TODO
            if rem < 0:
                return float('inf')
            if rem in memo:
                return memo[rem]
            # Try each coin
            min_coins = float('inf')
            for coin in coins:
                res = recurse(rem - coin)
                if res >= 0:
                    min_coins = min(min_coins, res + 1)
            
            memo[rem] = min_coins
            return min_coins
        
        result = recurse(amount)
        return result if result != float('inf') else -1

if __name__ == "__main__":
    coins = [2,5]
    amount = 2
    s = Solution()
    print(s.coinChange(coins, amount))
from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Handle edge case
        if amount == 0:
            return 0
        
        seen = {}
        queue = deque()
        # (amount, hops)
        queue.append((0,0))
        
        while queue:
            node = queue.popleft()
            for coin in coins:
                new_node = (coin + node[0], node[1] + 1)
                if new_node[0] == amount:
                    return new_node[1]
                elif new_node[0] < amount:
                    queue.append(new_node)

        # Queue is empty - no solutions
        return -1
                
         

            
        
        
if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    s = Solution()
    print(s.coinChange(coins, amount))
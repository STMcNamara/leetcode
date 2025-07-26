from collections import deque
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Handle edge case
        if amount == 0:
            return 0
        
        seen_amounts = set()
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
                    if new_node[0] not in seen_amounts:
                        queue.append(new_node)
                        seen_amounts.add(new_node[0])
                    

        # Queue is empty - no solutions
        return -1
                
         

            
        
        
if __name__ == "__main__":
    coins = [1,2,5]
    amount = 100
    s = Solution()
    print(s.coinChange(coins, amount))
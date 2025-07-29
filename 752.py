from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        # Handle edge case
        if "0000" in deadends:
            return -1

        seen = set()
        seen.add(('0000'))
        
        q = deque()
        q.append(('0000',0))
        
        while q:
            node = q.popleft()
            print(node)
            
            val = []
            for char in node[0]:
                val.append(int(char))

            # Evalaute the current node for found
            if node[0] == target:
                return node[1]

            for i in range(4):
                num = val[i]
                # Up increment
                if num == 9:
                    inc = 0
                else:
                    inc = num + 1

                new_val = val.copy()
                new_val[i] = inc
                new_str = ""
                for char in new_val:
                    new_str += str(char)

                up_node = (new_str, node[1] + 1)
                
                if up_node[0] not in seen and up_node[0] not in deadends:
                    q.append(up_node)
                    seen.add(up_node[0])    
                
                # Down increment
                if num == 0:
                    inc = 9
                else:
                    inc = num - 1

                new_val = val.copy()
                new_val[i] = inc
                new_str = ""
                for char in new_val:
                    new_str += str(char)

                down_node = (new_str, node[1] + 1)

                if down_node[0] not in seen and down_node[0] not in deadends:
                    q.append(down_node)
                    seen.add(down_node[0])

        return -1

# Test Area
if __name__ == "__main__":
    s = Solution()
    # deadends = ["0201","0101","0102","1212","2002"]
    # target = "0202"
    # # deadends = ["8888"]
    # # target = "0009"
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"]
    target = "8888"

    print(s.openLock(deadends, target))    
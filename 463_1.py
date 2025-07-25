from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Scan the grid
        perim = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                    if grid[row][col] == 1:
                        perim += 4
                        if row > 0 and grid[row - 1][col] == 1:
                            perim -= 2
                        if col > 0 and grid[row][col - 1] == 1:
                             perim -= 2

        return perim
                        
                          
    
# Test area
grid1 = [[1,1],[1,1]]
s = Solution()
print(s.islandPerimeter(grid1))
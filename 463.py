from collections import deque
from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Useful values
        rows = len(grid)
        cols = len(grid[0])

        # Find land!
        start_node = self.findLand(grid)

        # BFS and aggregate edges that are next to water
        queue = deque()
        queue.append(start_node)

        seen = set()
        seen.add(start_node)
        perimeter = 0
        
        # (Up, Right, Down, Left)
        directions = [(-1, 0), (0 , 1), (1, 0), (0, -1)]

        while queue:
            node_r, node_c = queue.popleft()
            for delta_r, delta_c in directions:
                neighour_row, neighbour_col = node_r + delta_r, node_c + delta_c
                # At either end of a row
                if 0 > neighour_row or neighour_row >= rows:
                    perimeter += 1
                # At either end of a column
                elif 0 > neighbour_col or neighbour_col >= cols:
                    perimeter += 1
                elif (neighour_row, neighbour_col) not in seen:
                    # Land case
                    if grid[neighour_row][neighbour_col] == 1:
                        queue.append((neighour_row, neighbour_col))
                        seen.add((neighour_row, neighbour_col))
                    # Water case
                    else:
                        perimeter += 1


        return perimeter
    
    def findLand(self, grid: List[List[int]]) -> tuple:
        rows = len(grid)
        cols = len(grid[0])

        # Find land!
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    start_node = (i, j)
                    return start_node
    
# Test area
grid1 = [[1,1],[1,1]]
s = Solution()
print(s.islandPerimeter(grid1))
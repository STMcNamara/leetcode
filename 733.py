from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Useful values
        rows = len(image)
        cols = len(image[0])
        
        # BFS for valus that are the same
        seen = set()
        queue = deque()
        queue.append((sr, sc))
        
        while queue:
            node = queue.popleft()
            neighbours = []
            # Above
            if node[0] != 0 and (node[0] - 1, node[1]) not in seen:
                neighbours.append((node[0] - 1, node[1]))
            # Below
            if node[0] != rows - 1:
                neighbours.append((node[0] + 1, node[1]))
            # LHS
            if node[1] != 0:
                neighbours.append((node[0], node[1] - 1))
            # RHS
            if node[1] != cols - 1:
                neighbours.append((node[0], node[1] + 1))
            print(neighbours)
        return

# Test Cases
grid1 = [[1,1,1],[1,1,0],[1,0,1]]
colour1 = 1
sc = 2
sr = 0
s = Solution()
s.floodFill(grid1, sr, sc, colour1)

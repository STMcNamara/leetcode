from collections import deque
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Useful values
        rows = len(image)
        cols = len(image[0])

        # Rember original colour
        org_col = image[sr][sc]
        
        # Set starting colour
        image[sr][sc] = color
        
        # BFS for valus that are the same
        seen = set()
        queue = deque()
        queue.append((sr, sc))
        
        while queue:
            node = queue.popleft()
            seen.add(node)

            neighbours = []
            # Above
            if node[0] != 0 and (node[0] - 1, node[1]) not in seen:
                neighbours.append((node[0] - 1, node[1]))
            # Below
            if node[0] != rows - 1 and (node[0] + 1, node[1]) not in seen:
                neighbours.append((node[0] + 1, node[1]))
            # LHS
            if node[1] != 0 and (node[0], node[1] - 1) not in seen:
                neighbours.append((node[0], node[1] - 1))
            # RHS
            if node[1] != cols - 1 and (node[0], node[1] + 1) not in seen:
                neighbours.append((node[0], node[1] + 1))

            for neighbour in neighbours:
                if image[neighbour[0]][neighbour[1]] == org_col:
                    image[neighbour[0]][neighbour[1]] = color
                    queue.append(neighbour)
                else:
                    seen.add(neighbour)


        return image

# Test Cases
grid1 = [[1,1,1],[1,1,0],[1,0,1]]
colour1 = 2
sc = 2
sr = 0
s = Solution()
print(s.floodFill(grid1, sr, sc, colour1))

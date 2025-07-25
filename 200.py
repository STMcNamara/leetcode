from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        viewed = set()
        
        n = 0

        island_count = 0
        
        # iterate over each element
        for row in grid:
            m = 0
            for val in row:
                # Skip viewed elements
                if (m,n) in viewed:
                    pass
                # Skip unviewed 0 elements and add to seen
                elif val == "0":
                    viewed.add((m,n))
                # Otherwise we have found an unseen 1
                else:
                # Initialise a queue with the starting node
                    queue = [(m,n)]
                
                # While queue is not empty
                    while queue:
                        # Get newest node and remove from queue and add to seen
                        node = queue.pop(0)
                        viewed.add(node)

                        # Get neighbours to right and down (above and left must've been seen)
                        # If "0" add to seen and move on
                        # If "1" add to queue
                        neighbours = []
                        # Right neighbour
                        if node[0] != len(row) - 1: # Avoid RHS boundary
                            rh_neighbour = (node[0] + 1, node[1])
                            if rh_neighbour not in viewed:
                                neighbours.append(rh_neighbour)
                        if node[0] != 0: # Avoid LHS boundary
                            lh_neighbour = (node[0] - 1, node[1])
                            if lh_neighbour not in viewed:
                                neighbours.append(lh_neighbour)
                        if node[1] != len(grid) - 1: # Avoid Bottom boundary
                            down_neighbour = (node[0], node[1] + 1)
                            if down_neighbour not in viewed:
                                neighbours.append(down_neighbour)
                        if node[1] != 0: # Avoid Top boundary
                            up_neighbour = (node[0], node[1] - 1)
                            if up_neighbour not in viewed:
                                neighbours.append(up_neighbour)

                        for neighbour in neighbours:
                            if grid[neighbour[1]][neighbour[0]]== "1":
                                queue.append(neighbour)
                            else:
                                viewed.add(neighbour)

                    island_count += 1
                # Increment along row
                m += 1
            # Increment down a row
            n += 1

        return island_count



if __name__ == "__main__":
    grid1 = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    grid2 = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    grid3 = [["1","1","1"],["0","1","0"],["1","1","1"]]
    s = Solution()
    print(s.numIslands(grid1))
    print(s.numIslands(grid2))
    print(s.numIslands(grid3))

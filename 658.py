from collections import deque
from typing import List
from bisect import bisect_left

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # First simple binary search

        insertion_point = bisect_left(arr, x) # Equal or closest smaller index
        # Handle edge case
        if insertion_point > len(arr):
            cls_eql_smlr = len(arr) - 1
        else:
            cls_eql_smlr = insertion_point

        # Sliding window to find nearest values
        lp = cls_eql_smlr - 1
        rp = cls_eql_smlr

        res = deque()
        while len(res) < k:
            # Check for LHS bounding case
            if lp < 0:
                res.append(arr[rp])
                rp += 1
            elif rp >= len(arr):
                res.appendleft(arr[lp])
                lp -= 1            
            # Check if lp value is closer
            elif abs(arr[lp] - x) <= abs(arr[rp] - x):
                res.appendleft(arr[lp])
                lp -= 1
            else:
                res.append(arr[rp])
                rp += 1

        return list(res)

    
if __name__ == "__main__":
    # Arrange
    # Example 1
    arr = [1,2,3,4,5]
    k = 4
    x = 3

    # Act
    s = Solution()
    print(s.findClosestElements(arr, k, x))

    # Asset

import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lp = 0
        rp = len(nums) - 1

        while lp <= rp:
            mid = (lp + rp) // 2

            # Found case
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                rp = mid - 1
            else:
                lp = mid + 1

        # We didn't find
        return -1
        
    
if __name__ =="__main__":
    s = Solution()
    test_list = [-1,0,3,5,9,12]
    target = 12


    print(s.search(test_list, target))
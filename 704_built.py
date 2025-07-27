from typing import List
from bisect import bisect_left

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = bisect_left(nums, target)
        if nums[i] == target and i != len(nums):
            return i
        
        return -1
        
    
if __name__ =="__main__":
    s = Solution()
    test_list = [-1,0,3,5,9,12]
    target = 12


    print(s.search(test_list, target))
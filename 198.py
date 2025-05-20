from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Position starting at last house
        pos = len(nums)-1
        result = self.n_pos_max(nums, pos)
        return result


    def n_pos_max(self, nums, pos):    
        # TODO - Works - add in momoization
        if pos == 0:
            rob_max = nums[0]
        elif pos == 1:
            rob_max = max(nums[pos], nums[pos-1])
        else:
            rob_max =max(nums[pos]+self.n_pos_max(nums, pos-2), self.n_pos_max(nums, pos-1))
        
        return rob_max
    
solution = Solution()
print(solution.rob([2,1,2,1000]))
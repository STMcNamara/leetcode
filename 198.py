from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Position starting at last house
        pos = len(nums)-1
        result = self.n_pos_max(nums, pos, dict())
        return result


    def n_pos_max(self, nums, pos, memo):    
        # TODO - Works - add in momoization
        if pos in memo:
            return memo[pos]
        
        if pos == 0:
            rob_max = nums[0]
            memo[0] = rob_max
        elif pos == 1:
            rob_max = max(nums[pos], nums[pos-1])
            memo[1] = rob_max
        else:
            rob_max =max(nums[pos]+self.n_pos_max(nums, pos-2, memo), self.n_pos_max(nums, pos-1, memo))
            memo[pos] = rob_max
        
        return rob_max
    
solution = Solution()
print(solution.rob([2,7,9,3,1]))
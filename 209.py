from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lp = 0
        rp = 0
        size = len(nums)
        shortest = len(nums)
        # Evaluate until first a solution is found
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            if tot >= target:
                shortest = i + 1
                break

        if tot < target:
            return 0
        
        # Sliding window
        lp = 0
        rp = shortest - 1

        while rp < size:
            tot = 0
            for i in range(lp, rp + 1):
                tot += nums[i]

            if tot < target:
                if lp + 1 == size: # We've reached the end and don't have target left
                    return shortest
                
                # As we're below target - advance and keep window
                lp += 1
                rp += 1

            else:
                # As we're above target, must be no worse than previous smallest
                shortest = rp - lp + 1
                # Try again with a smaller window
                lp += 1
        
        return shortest
    
s = Solution()
target = 10
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))
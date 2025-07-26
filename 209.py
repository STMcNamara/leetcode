from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        lp = 0
        shortest = size + 1
        tot = 0
        for rp in range(size):
            tot += nums[rp]
            while tot >= target:
                if rp - lp + 1 < shortest:
                    shortest = rp - lp + 1

                tot -= nums[lp]
                lp += 1

        if shortest == size + 1:
            return 0
        else:
            return shortest
                
    
s = Solution()
target = 10
nums = [2,3,1,2,4,3]
print(s.minSubArrayLen(target, nums))
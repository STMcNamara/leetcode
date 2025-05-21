from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Handle edge cases
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return nums1 
         
        elif n == 0:
            return nums1 
        
        pos_m = m-1
        pos_n = n-1      

        for i in range(m+n-1, -1, -1):
            # Check for stopping conditions
            if pos_m == -1:
                nums1[i] = nums2[pos_n]
                pos_n -= 1

            elif pos_n == -1:
                break
            
            # Main iteration
            elif nums1[pos_m] > nums2[pos_n]:
                nums1[i] = nums1[pos_m]
                pos_m -= 1
            else:
                nums1[i] = nums2[pos_n]
                pos_n -= 1



        return nums1 

solution = Solution()
print(solution.merge([2,0], 1, [1], 1))
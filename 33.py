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

            # If LHS is sorted
            if nums[lp] <= nums[mid]:
                # Check if target present in sorted LHS
                if nums[lp] <= target <= nums[mid]:
                    # If present - bisect LHS
                    rp = mid - 1
                else:
                    # If absent - try the unsorted RHS side
                    lp = mid + 1
            else:
                # Check if target present in sorted RHS
                if nums[mid+1] <= target <= nums[rp]:
                    # If present - bisect RHS
                    lp = mid + 1
                else:
                    # If absent - Try the Unsorted LHS
                    rp = mid -1



        return -1

if __name__ == "__main__":
    s = Solution()
    # nums_test = [4,5,6,7,0,1,2]
    # target = 0

    # nums_test = [1]
    # target = 0

    nums_test = [3,4,5,6,1,2]
    target = 2
    print(s.search(nums=nums_test, target=target))
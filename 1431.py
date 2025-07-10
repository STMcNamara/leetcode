from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_baseline = max(candies)
        output = []

        for i in candies:
            if i + extraCandies >= max_baseline:
                output.append(True)
            else:
                output.append(False)

        return output

if __name__ == "__main__":
    solution = Solution()
    output1 = solution.kidsWithCandies([2,3,5,1,3], 3)
    output2 = solution.kidsWithCandies([4,2,1,1,2], 1)

    
    print(output1)
    print(output2)

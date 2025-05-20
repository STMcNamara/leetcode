class Solution:
    memo = dict()

    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        else:
            if n in self.memo:
                return self.memo[n]
            else:
                result = self.climbStairs(n-1) + self.climbStairs(n-2)
                self.memo[n] = result

                return result

solution = Solution()
print(solution.climbStairs(44))
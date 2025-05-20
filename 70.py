class Solution:
    memo = dict()

    def climbStairs(self, n: int) -> int:
        if n > 1:
            if n-1 in self.memo:
                n_1 = self.memo[n-1]
            else:
                n_1 = self.climbStairs(n-1)
                self.memo[n-1] = n_1

            if n-2 in self.memo:
                n_2 = self.memo[n-2]
            else:
                n_2 = self.climbStairs(n-2)
                self.memo[n-2] = n_2
            
            result = n_1  + n_2
        else:
            result = 1

        return result
     
solution = Solution()
print(solution.climbStairs(44))
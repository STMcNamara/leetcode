class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            total=0
            n_2 = 0
            n_1 = 1
            for i in range(n-1):
                total = n_2 + n_1
                n_2 = n_1
                n_1 = total


        return total
    
# Test Area
solver = Solution()
print(solver.fib(4))

class Solution:
    store = dict()
    def fib(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            if n in self.store:
                return self.store[n]
            else:
                result = self.fib(n-1)+self.fib(n-2)
                self.store[n] = result
                return result
            
# Test Area
solver = Solution()
print(solver.fib(4))


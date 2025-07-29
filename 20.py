class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}' : '{' , ']' : '['}
        stack = []

        for char in s:
            # Open bracket case
            if char in bracket_map.values():
                stack.append(char)
            # Closed bracket case - no stack
            elif not stack or stack[-1] != bracket_map[char]:
                return False
            else:
                stack.pop()
        
        if stack:
            return False
        else:
            return True
                
if __name__ == "__main__":
    s = Solution()
    brackets = "()"
    print(s.isValid(brackets))
                




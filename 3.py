class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        if len(s) == 0:
            return 0
       
        longest_len = 1
        longest_str = ""
       
        current_len = 1
        current_str = s[0]        
        for i in range(1, len(s)):
            if s[i] not in current_str:
                current_str +=s[i]
                current_len += 1
               
                if current_len > longest_len:
                    longest_len = current_len
                    longest_str = current_str
                   
            else:
                # Figure out the the last place the that the current letter appearred
                letter = ""
                index = i
                while letter != s[i]:
                    index -= 1
                    letter = s[index]
               
                current_str = s[index+1:i+1]
                current_len = len(current_str)

        return longest_str

solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))
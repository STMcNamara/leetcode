class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       
        if len(s) == 0:
            return 0
       
        longest_len = 1
        longest_str = ""
       
        window_start_pos = 0
        current_str_len = 1

        for s_pos in range(1, len(s)):
            # Iterate in reverse over sliding window
            for j in range(s_pos-1, window_start_pos-1, -1):
                # print("s_pos: " + str(s_pos))
                # print("window_pos: " + str(j))

                if s[j] == s[s_pos]:
                    current_str_len = s_pos - j
                    window_start_pos = j + 1

                else:
                    current_str_len  = s_pos - window_start_pos + 1

            if current_str_len > longest_len:
                longest_len = current_str_len

            # print(current_str_len)    

        return longest_len

solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))
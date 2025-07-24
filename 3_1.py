class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l_ind = 0

        last_seen_letter = {}
        longest_str = 0
        current_str = 0

        for r_ind in range(len(s)):
            # Check if current letter has been seen
            if s[r_ind] in last_seen_letter:
                letter_prev_ind = last_seen_letter[s[r_ind]]
            else:
                letter_prev_ind = -1

            if letter_prev_ind < l_ind:
                current_str = r_ind - l_ind + 1

            else:
                current_str = r_ind - letter_prev_ind
                l_ind  = letter_prev_ind + 1

            if current_str > longest_str:
                longest_str = current_str

            # Update the last position
            last_seen_letter[s[r_ind]] = r_ind

        return longest_str





solution = Solution()
print(solution.lengthOfLongestSubstring("dvdf"))
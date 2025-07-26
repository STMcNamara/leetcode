class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        lp = 0
        size = len(s)
        window = dict()
        longest = 1
        for rp in range(size):
            # Add rp element to dict
            if s[rp] in window:
                window[s[rp]] += 1
            else:
                window[s[rp]] = 1

            # Check conditions
            window_size = rp - lp + 1
            most_freq = max(window.values())

            if most_freq + k >= window_size: # We can go bigger
                longest = max(longest, window_size)
            else: # We need to shrink and move on
                window[s[lp]] -= 1
                lp += 1
                

        return longest
    
if __name__ == "__main__":
    solution = Solution()
    k = 1
    s = "AABABBA"
    print(solution.characterReplacement(s, k))
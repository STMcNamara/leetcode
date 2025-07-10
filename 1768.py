class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # Starting pointer position
        pos_1 = 0
        pos_2 = 0
        len_1 = len(word1)
        len_2 = len(word2)

        merged = ""
        # Evaluate while we are not at the end of either list
        while pos_1 < len_1 and pos_2 < len_2:
            merged += word1[pos_1]  + word2[pos_2]

            pos_1 += 1
            pos_2 += 1

        # Handle remaining letters
        if pos_1 == len_1 and pos_2 != len_2:
            merged += word2[pos_2:len_2]
        elif pos_2 == len_2 and pos_1 != len_1:
            merged+= word1[pos_1:len_1]

        return merged

if __name__ == "__main__":
    solution = Solution()
    output1 = solution.mergeAlternately("abc", "pqr")
    output2 = solution.mergeAlternately("ab", "pqrs")
    output3 = solution.mergeAlternately("abcd", "pq")
    
    print(output1)
    print(output2)
    print(output3)

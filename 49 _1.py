from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # represent each word as a dict
        words_dict = {}
      
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in words_dict.keys():
                words_dict[sorted_word].append(word)
            else:
                words_dict[sorted_word] = [word]

        return list(words_dict.values())
    
s = Solution()
inputs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(inputs))
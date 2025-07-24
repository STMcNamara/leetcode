from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # represent each word as a dict
        words_dict = {}
      
        for word in strs:
            chars_dict = {}
            for char in word:
                if char in chars_dict:
                    chars_dict[char] += 1
                else:
                    chars_dict[char] = 1
            word_hash = hash(frozenset(chars_dict.items()))
            if word_hash in words_dict:
                words_dict[word_hash].append(word)
            else:
                words_dict[word_hash] = [word]   

      
      
        return list(words_dict.values())
    
s = Solution()
inputs = ["eat","tea","tan","ate","nat","bat"]
print(s.groupAnagrams(inputs))
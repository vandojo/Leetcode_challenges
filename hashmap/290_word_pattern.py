'''Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
'''

# Solution

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        items = s.split(' ')
        hashMap = {}

        if len(items) != len(pattern):
            return False
        
        for i in range(len(pattern)):
            if pattern[i] in hashMap:
                if hashMap[pattern[i]] != items[i]:
                    return False
            else:
                if items[i] in hashMap.values():
                    return False
                else:
                    hashMap[pattern[i]] = items[i]
        return True


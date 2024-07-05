'''Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
'''
# Solution
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        hashMap = Counter(magazine)
        for letter in ransomNote:
            if letter not in hashMap or hashMap[letter] <= 0:
                return False
            else:
                hashMap[letter] -= 1        
        
        return True


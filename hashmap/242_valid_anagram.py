'''Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false

'''

# Solution:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = defaultdict(int)

        for letter in s:
            hashMap[letter] += 1
        for letter in t:
            if letter not in hashMap or hashMap[letter] == 0:
                return False
            hashMap[letter] -= 1

        return True
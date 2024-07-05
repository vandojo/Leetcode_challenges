'''Given two strings s and t of lengths m and n respectively, return the minimum window
substring
of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

 

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
'''

# Solution
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        hashMapT = defaultdict(int)

        for letter in t:
            hashMapT[letter] += 1
        
        minLength = len(hashMapT)

        left = 0
        right = 0
        charsCorrect = 0
        windowChars = defaultdict(int)
        minWindow = [-1, 0, 0]

        while right < len(s):
            letter = s[right]
            windowChars[letter] += 1
            
            # true if letter exists and has same count in both dictionaries
            if letter in hashMapT and windowChars[letter] == hashMapT[letter]:
                charsCorrect += 1
            
            while left <= right and charsCorrect == minLength:
                letter = s[left]

                if minWindow[0] == -1 or right - left + 1 < minWindow[0]:
                    minWindow[0] = right - left + 1
                    minWindow[1] = left
                    minWindow[2] = right
                
                windowChars[letter] -= 1

                if letter in hashMapT and windowChars[letter] < hashMapT[letter]:
                    charsCorrect -= 1
                
                left += 1
            
            right += 1
        
        if minWindow[0] == -1:
            return ""
        else:
            return s[minWindow[1]:minWindow[2]+1]
'''Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''

# Solution
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        lPntr = 0
        longestSubStr = 0
        charSet = set()

        for rPntr in range(len(s)):
            while s[rPntr] in charSet:
                charSet.remove(s[lPntr])
                lPntr += 1
            # add current char to set 
            charSet.add(s[rPntr])

            # change length substring
            longestSubStr = max(longestSubStr, rPntr - lPntr + 1)
        
        return longestSubStr
'''Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

 '''

# Solution
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # challenge is called two pointers so lets use two pointers
        sPntr = 0
        tPntr = 0

        while sPntr < len(s) and tPntr < len(t):
            if s[sPntr] == t[tPntr]:
                sPntr += 1
            tPntr += 1
        return sPntr == len(s)
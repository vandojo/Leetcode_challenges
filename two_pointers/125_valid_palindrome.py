'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome'''

# Solution
import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sFormatted = re.sub("\W", '', s.lower())
        sFormatted = re.sub("_", '', sFormatted)
        sReversed = sFormatted[::-1]

        for i in range(len(sFormatted)):
            if sFormatted[i] != sReversed[i]:
                return False
        return True
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

 

Constraints:

    1 <= strs.length <= 200
    0 <= strs[i].length <= 200
    strs[i] consists of only lowercase English letters.
'''

# Solution
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""   
        
        # loop through letters in shortest word
        for i in range(len(min(strs))):
            # get current letter
            letter = strs[0][i]

            # if all words have that letter in that position
            # add it to the prefix, otherwise return the current
            # prefix
            if all(word[i] == letter for word in strs):
                prefix += letter
            else:
                break
        return prefix

        
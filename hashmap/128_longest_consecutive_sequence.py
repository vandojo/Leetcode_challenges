'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
'''

# Solution

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sequence = 0
        longest = 0
        numbers = set(nums)

        for num in nums:
            if num - 1 not in numbers:
                sequence = 1

                while num + sequence in numbers:
                    sequence += 1
                
                longest = max(sequence, longest)
        return longest
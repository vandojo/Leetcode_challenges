'''
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
'''

# Solution 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        majority = nums[0]
        n = len(nums)
        
        for i in range(1, n):
            if nums[i] != majority:
                count -= 1
            else:
                count += 1
            
            if count == 0:
                majority = nums[i]
                count += 1
        
        return majority

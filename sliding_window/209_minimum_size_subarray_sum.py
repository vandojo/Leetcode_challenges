'''
Given an array of positive integers nums and a positive integer target, return the minimal length of a
subarray
whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.

Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
'''

# Solution
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        if sum(nums) < target: return 0

        left = 0
        currentSum = 0
        result = len(nums)

        # go through the list
        for right, val in enumerate(nums):
            # add current val to the currenSum
            currentSum += val
            while currentSum >= target:
                # pick the shortest sub array
                result = min(result, right - left + 1)

                # remove leftmost value from currentSum
                # and increment left pointer
                currentSum -= nums[left]
                left += 1
        return result
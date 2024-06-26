'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

'''



# Solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        answer = [1] * n

        # calculate all prefix values
        # start at 1 b/c first element does not have a prefix
        for i in range(1, n):
            # current prefix is equal to previous prefix with additional number
            prefix[i] = prefix[i-1] * nums[i-1]
        
        # calculate all suffixes
        # second to last index is the last one with a suffix
        # go back to zero
        for j in range(n-2, -1, -1):
            suffix[j] = suffix[j+1] * nums[j+1]
        
        for k in range(n):
            answer[k] = prefix[k]  * suffix[k]
        
        return answer
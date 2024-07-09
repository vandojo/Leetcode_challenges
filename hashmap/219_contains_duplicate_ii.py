'''Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.

 

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
'''

# Solution

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hashMap = {}

        for key, val in enumerate(nums):

            if val in hashMap and abs(key - hashMap[nums[key]]) <= k:
                return True

            
            hashMap[val] = key
        
        return False



        
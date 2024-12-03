'''Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space.'''

# Solution 1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hash_map = {}
        

        for n in nums:
            if n in hash_map.keys():
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        return list(hash_map.keys())[list(hash_map.values()).index(1)]

# Solution 2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        tmp = 0

        for n in nums:
            ans = ans ^ n & ~tmp
            tmp = tmp ^ n & ~ans
        return ans
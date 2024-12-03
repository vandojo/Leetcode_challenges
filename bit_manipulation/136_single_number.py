'''Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.'''


# Solution1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        hash_map = {}
        

        for n in nums:
            if n in hash_map.keys():
                hash_map[n] += 1
            else:
                hash_map[n] = 1
        return list(hash_map.keys())[list(hash_map.values()).index(1)]

       

# solution 2
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0
        for n in nums:
            ans ^= n
        return ans


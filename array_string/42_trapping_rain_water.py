'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
'''


# Solution
class Solution:
    def trap(self, height: List[int]) -> int:

        # two pointers:
        # left pointer start fromt beginning of height
        left = 0
        # right pointer start from end of height
        right = len(height) -1

        left_max = height[left]
        right_max = height[right]

        amt_water = 0

        while left != right:

            if left_max <= right_max:
                left += 1
                if height[left] > left_max:
                    left_max = height[left]
                amt_water += left_max - height[left]
            else:
                right -= 1
                if height[right] > right_max:
                    right_max = height[right]
                amt_water += right_max - height[right]
        return amt_water

'''You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.'''

# Solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        lPntr = 0
        rPntr = len(height) - 1
                
        maxArea = 0

        while lPntr != rPntr:
            area = (rPntr - lPntr) * min(height[lPntr], height[rPntr])
            maxArea = max(maxArea, area)

            if height[lPntr] < height[rPntr]:
                lPntr += 1
            else:
                rPntr -= 1
            
            
            
        return maxArea
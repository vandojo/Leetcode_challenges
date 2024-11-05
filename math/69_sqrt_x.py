'''description
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

    For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.



'''

# solution

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:

            return 0
        # conduct binary search
        # mid * mid == x return mid
        # mid * mid < x increment lPntr to mid + 1
        # mid * mid > x decrement rPntr to mid - 1
        lPntr = 1
        rPntr = x
        while lPntr <= rPntr:
            mid = (lPntr + rPntr) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lPntr = mid + 1
            else:
                rPntr = mid - 1
        return rPntr 
       
       
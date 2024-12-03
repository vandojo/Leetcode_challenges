'''Given two integers left and right that represent the range [left, right], return the bitwise AND of all numbers in this range, inclusive'''


# Solution
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:

        amt = 0
        while left < right:
            left >>= 1
            right >>= 1
            amt += 1
        return left << amt
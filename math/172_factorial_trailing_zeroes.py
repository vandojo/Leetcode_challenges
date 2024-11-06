'''description

Given an integer n, return the number of trailing zeroes in n!.

Note that n! = n * (n - 1) * (n - 2) * ... * 3 * 2 * 1.
'''

# Solution
class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        ans = 0
        while n // 5:
            ans += n // 5

            n /= 5
        


        return int(ans)


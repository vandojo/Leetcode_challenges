'''Given a positive integer n, write a function that returns the number of
set bits
in its binary representation (also known as the Hamming weight).'''


# solution
class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0

        for i in range(32):
            if n >> i & 1:
                ans += 1
        
        return ans

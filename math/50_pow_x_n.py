''' description

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

'''

# Solution
class Solution:

    def toPow(self, x: float, n: int):
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        ans = self.toPow(x, n // 2)
        ans *= ans

        if n % 2 == 1:
            return ans * x
        return ans
        
    def myPow(self, x: float, n: int) -> float:

        output = self.toPow(x, abs(n))
        if n >= 0:
            return output
        else:
            return 1 / output

        total = x
        for i in range(1, n, 1):
            total *= x
        return total
        

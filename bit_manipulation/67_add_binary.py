'''Given two binary strings a and b, return their sum as a binary string.'''

# solution 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        ans = []
        c = 0
        idA = len(a) - 1
        idB = len(b) - 1
        while idA >= 0 or idB >= 0 or c == 1:
            if idA >= 0:
                c += int(a[idA])
                idA -= 1
            if idB >= 0:
                c += int(b[idB])
                idB -= 1
            ans.append(str(c % 2))
            c = c // 2
        
        return "".join(ans[::-1])

        

# solution 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:


        return bin(int(a,2) + int(b,2))[2:]

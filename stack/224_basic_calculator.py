'''
Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

'''

# SOLUTION

class Solution:
    def calculate(self, s: str) -> int:
        answer = 0
        curr_n = 0
        sign = 1
        stack = []

        for symbol in s:
            if symbol.isdigit():
                curr_n = curr_n * 10 + int(symbol)
            elif symbol in "+-":
                answer += curr_n * sign
                curr_n = 0
                
                if symbol == "-":
                    sign = -1
                else:
                    sign = 1
            elif symbol == "(":
                stack.append(answer)
                stack.append(sign)
                answer = 0
                sign = 1
            elif symbol == ")":
                answer += curr_n * sign
                answer *= stack.pop() 
                answer += stack.pop()
                curr_n = 0
                
        
        
        return answer + curr_n * sign

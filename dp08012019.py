# This problem was recently asked by Uber:

# Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses in the program are balanced. Every opening bracket must have a corresponding closing bracket. We can approximate this using strings. 

# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. 
# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.

class Solution:
    def isValid(self, s):
        # Fill this in.
        stack = []
        open_list = ["[","{","("] 
        close_list = ["]","}",")"]

        for i in s: 
            if i in open_list: 
                stack.append(i) 
            elif i in close_list: 
                pos = close_list.index(i) 
                # compare with the top of the stack
                if ((len(stack) > 0) and (open_list[pos] == stack[len(stack)-1])):
                    stack.pop() 
                else: 
                    return False

        if len(stack) == 0: 
            return True
        else:
            return False

# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))
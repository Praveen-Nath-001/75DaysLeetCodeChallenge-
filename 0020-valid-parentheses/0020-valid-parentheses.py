class Solution:
    def isValid(self, s: str) -> bool:
        result_stack = []
        for char in s:
            if char in "({[":
                result_stack.append(char)
            else:
                if not result_stack:
                    return False 

                top = result_stack.pop()
                if char == ')' and top != '(':
                    return False 
                if char == '}' and top != '{':
                    return False 
                if char == ']' and top != '[':
                    return False 
        return not result_stack 
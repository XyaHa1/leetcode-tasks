class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' and len(stack) > 0 and stack[-1] != '(':
                return False
            elif i == '}' and len(stack) > 0 and stack[-1] != '{':
                return False
            elif i == ']' and len(stack) > 0 and stack[-1] != '[':
                return False

            if i == ')' or i == '}' or i == ']':
                if len(stack) > 0:
                    stack.pop()
                else:
                    return False

        return len(stack) == 0

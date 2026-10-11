class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        missing = {")" : "(","}" : "{","]" : "[",}
    
        for char in s:
            if char in missing:
                if stack and stack[-1] == missing[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return not stack
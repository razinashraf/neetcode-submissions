class Solution:
    def isValid(self, s: str) -> bool:
        dict = {"}":"{","]":"[",")":"("}
        stack = []
        for char in s:
            if char in dict:
                if stack and stack[-1] == dict.get(char):
                    stack.pop()
                    continue
                return False
            stack.append(char)
        
        if not stack:
            return True
        return False

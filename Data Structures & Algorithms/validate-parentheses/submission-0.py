class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closeOpen ={")":"(","}":"{","]":"["}
        for c in s: 
            if c in "({[":
                stack.append(c)
            elif c in ")}]":
                if not stack or stack[-1]!=closeOpen[c]:
                    return False
                stack.pop()
                
        return len(stack)==0
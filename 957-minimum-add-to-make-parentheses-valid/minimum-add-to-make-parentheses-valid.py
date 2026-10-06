class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack=[]
        op=0
        cl=0
        for i in s:
            if i=='(':
                stack.append(i)
                op+=1
            elif i==')'and stack and stack[-1]=='(' :
                op-=1
                stack.pop()
            else:
                cl+=1
        return op+cl
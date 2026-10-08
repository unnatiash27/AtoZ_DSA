class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        op=0
        cl=0
        ans=""
        for i in range(len(s)):
            if s[i]=="(":
                op+=1
                if op>1:
                    ans+="("
            else:
                cl+=1
                if cl<op:
                    ans+=")"
                if op==cl:
                    op=0
                    cl=0
        return ans
            

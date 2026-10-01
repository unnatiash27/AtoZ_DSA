class Solution:
    def isValid(self, s: str) -> bool:
        stc=[]
        for i in s:
            if i == '(' or i=='{' or i=='[':
                stc.append(i)
            else:
                if not stc:
                    return False 
                top=stc.pop()
                if i==')' and top!='(':
                    return False
                elif i=='}' and top!='{':
                    return False
                elif i==']' and top!='[':
                    return False
        if len(stc)==0:
            return True
        else:
            return False
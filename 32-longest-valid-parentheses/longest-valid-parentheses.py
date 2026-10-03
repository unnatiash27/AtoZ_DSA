class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # stack=[]
        # cnt=0
        # for i in s:
        #     if not stack:
        #         stack.append(i)
        #     elif stack[-1]== "(" and i == ")":
        #         stack.pop()
        #         cnt+=2
        #     else:
        #         stack.pop()
        #         stack.append(i)
        #         cnt=0
        # return cnt

        stk=[-1]
        ans=0
        for i in range(0,len(s)):
            if s[i]=="(":
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    ans=max(ans, i-stk[-1])

        return ans
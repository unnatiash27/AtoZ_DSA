class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack=[0]
        for i in s:
            if i =='(':
                stack.append(0)
            else:
                x=stack.pop()
                if x==0:
                    stack.append(stack.pop()+1)
                else:
                    stack.append(stack.pop() + x*2)

        return stack.pop()
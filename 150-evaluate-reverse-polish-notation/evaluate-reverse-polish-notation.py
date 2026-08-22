class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st=[]
        for i in tokens:
            if i =='+':
                a=int(st[-1])
                st.pop()
                b=int(st[-1])
                st.pop()
                st.append(a+b)
            elif i =='-':
                a=int(st[-1])
                st.pop()
                b=int(st[-1])
                st.pop()
                st.append(b-a)
            elif i =='*':
                a=int(st[-1])
                st.pop()
                b=int(st[-1])
                st.pop()
                st.append(a*b)
            elif i =='/':
                a=int(st[-1])
                st.pop()
                b=int(st[-1])
                st.pop()
                st.append(int(b/a))
            else:
                st.append(i)
        return int(st[0])
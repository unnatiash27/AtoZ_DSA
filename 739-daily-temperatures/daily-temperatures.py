class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        st=[]
        ans=[0]*len(temp)
        for i in range(len(temp)-1,-1,-1):
            while st and temp[st[-1]] <= temp[i]:
                st.pop()
            if st :
                ans[i]=st[-1]-i
            st.append(i)
        return ans
# this i did on my own took 1 whole day!
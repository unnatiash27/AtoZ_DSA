class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:

        ans=[]
        newst=newInterval[0]
        newend=newInterval[1]

        for i,j in intervals:
            if j<newInterval[0]:
                # ans.append(intervals)
                ans.append([i,j])
            elif i>newInterval[1]:
                ans.append(newInterval)
                newInterval=[i,j]
            else:
                newInterval[0]=min(newInterval[0],i)
                newInterval[1]=max(newInterval[1],j)
        ans.append(newInterval)
        return ans

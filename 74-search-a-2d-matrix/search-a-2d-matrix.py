class Solution:
    def searchMatrix(self, mat: List[List[int]], target: int) -> bool:
        n=len(mat)
        m=len(mat[0])


        # TLE
        # for i in range(0,n):
        #     for j in range(0,m):
        #         if mat[i][j]==target:
        #             return True
        #             break
        # return False


        # staircase method
        # i=0
        # j=m-1
        # while i<n and j>=0:
        #     if mat[i][j]==target:
        #         return True
        #     elif target>mat[i][j]:
        #         i+=1
        #     else:
        #         j-=1
        # return False


        # Treating whole array as flat
        low=0
        high=n*m-1
        while low<=high:
            mid=(low+high)//2
            i=mid//m
            j=mid%m

            if mat[i][j]==target:
                return True
            elif mat[i][j]<target:
                low=mid+1
            else:
                high=mid-1
        return False
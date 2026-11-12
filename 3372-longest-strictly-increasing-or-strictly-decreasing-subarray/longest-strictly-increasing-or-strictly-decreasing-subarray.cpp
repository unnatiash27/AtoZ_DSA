class Solution {
public:
    int longestMonotonicSubarray(vector<int>& nums) 
    {
        int n=nums.size();
        int ans=1;
        int i=0,j=1;
        while(j<n)
        {
            if(nums[j]>nums[j-1])
            j++;
            else
            {
                i=j;
                j++;
            }
            ans=max(ans,j-i);
        }
        i=0,j=1;
        while(j<n)
        {
            if(nums[j]<nums[j-1])
            j++;
            else
            {
                i=j;
                j++;
            }
            ans=max(ans,j-i);
        }
        return ans;
    }
};
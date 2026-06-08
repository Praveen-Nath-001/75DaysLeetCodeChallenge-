class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub=[]
        for i in nums:
            left,right=0,len(sub)
            while left<right:
                mid=(left+right)//2
                if(sub[mid]<i):
                    left=mid+1
                else:
                    right=mid
            if(left==len(sub)):
                sub.append(i)
            else:
                sub[left]=i
        return len(sub)
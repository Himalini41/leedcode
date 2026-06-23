class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        c=0
        v=[]
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
                v.append(c)
            else:
                c=0
        if len(v)>0:
            return max(v)
        else:
            return 0
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        v=[]
        c=0
        for i in range(len(nums)):
            if nums[i]==1:
                c+=1
            else:
                v.append(c)
                c=0
        v.append(c)
        return max(v)       
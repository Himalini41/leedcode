class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        v=[]
        h=[]
        g=[]
        for i in range(len(nums)):
            if nums[i]<0:
                v.append(nums[i])
            elif nums[i]>=1:
                h.append(nums[i])
        g.append(len(v))
        g.append(len(h))
        return max(g)
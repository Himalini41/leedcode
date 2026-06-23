class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        a=[]
        b=[]
        for i in range(len(nums)):
            if nums[i]>0:
                a.append(nums[i])
            elif nums[i]<0:
                b.append(nums[i])
        return max(len(a),len(b))
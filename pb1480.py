class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        v=[]
        c=0
        for i in nums:
            c+=i
            v.append(c)
        return v
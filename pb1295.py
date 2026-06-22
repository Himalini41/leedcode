class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        v=[]
        c=0
        for i in range(len(nums)):
            v.append(len(str(nums[i])))
            if v[i]%2==0:
                c+=1
        return (c)
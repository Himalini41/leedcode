class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=[]
        for i in range(len(nums)):
            n.append(sum(nums[0:((len(nums)-i))]))
        return n[::-1]
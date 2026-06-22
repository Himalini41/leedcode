class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        g=sorted(nums)
        for i in range(len(nums)):
            nums[i]=g[i]
        
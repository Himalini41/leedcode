class Solution:
    def search(self, nums: List[int], target: int) -> int:
        c=len(nums)//2
        
        for i in range(len(nums)):
            if nums[i:c]==target:
                return nums.index(i)
            elif nums[c+1:i]==target:
                return nums.index(i)
            else:
                return i
        
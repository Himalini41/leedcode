class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(nums)
        g=nums[len(nums)-k:]
        h=nums[:len(nums)-k]
        s=(g+h)
        for i in range(len(nums)):
            nums[i]=s[i]
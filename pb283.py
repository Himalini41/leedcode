class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        v=[]
        b=[]
        for i in nums:
            if i!=0:
                b.append(i)
            else:
                v.append(i)
        print(*b,*v)
        """
        c=nums.count(0)
        for i in nums:
            if i==0:
                nums.remove(i)
                nums.append(i)
        
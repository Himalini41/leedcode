class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        v=[]
        for i in nums:
            if i!=val:
                v.append(i)
        nums[:]=v
        return len(v)
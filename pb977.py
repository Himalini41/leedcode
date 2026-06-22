class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        v=[]
        for i in nums:
            v.append(i*i)
        return sorted(v)
       
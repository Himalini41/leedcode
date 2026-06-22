class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        g=list(set(nums))
        g=sorted(g)
        g=g[::-1]
        if len(g)>=3:
            return g[2]
        else:
            return max(nums)
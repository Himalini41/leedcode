class Solution:
    def maxArea(self, height: List[int]) -> int:
        m=0
        l=0
        r=len(height)-1
        while l<r:
            w=r-l
            h=min(height[l],height[r])
            m=max(m,w*h)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return m
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m=nums1[0:m]
        n=nums2[0:n]
        g=sorted(n+m)
        for i in range(len(g)):
            nums1[i]=g[i]
       
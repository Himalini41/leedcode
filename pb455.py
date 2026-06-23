class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g=sorted(g)
        s=sorted(s)
        c=0
        i=0
        j=0
        print(g)
        while i<len(g) and j<len(s):
            if g[i]<=s[j]:
                c+=1
                i+=1
                j+=1
            else:
                j+=1
        return c
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s=list(s)
        a=[]
        for i in range(len(s)):
            if s[i]==c:
                a.append(i)
        h=[]
        for i in range(len(s)):
            m=1000000
            for j in a:
                if abs(i-j)<m:
                    m=abs(i-j)
            h.append(m)
        return h
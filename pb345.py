class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        l=0
        r=len(s)-1
        while l<r:
            if s[l] not in 'aeiouAEIOU':
                l+=1
                continue
            if s[r] not in 'aeiouAEIOU':
                r-=1
                continue
            s[l],s[r]=s[r],s[l]
            l+=1
            r-=1
        return "".join(s)
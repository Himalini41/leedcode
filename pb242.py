class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c=0
        v=''
        for i in s:
            if i in t and s.count(i)==t.count(i):
                v+=i
                c+=1
        print(v)
        if c==len(s) and c==len(t) and len(v)==len(s) and len(v)==len(t):
            return True
        else:
            return False
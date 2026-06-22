class Solution:
    def isPalindrome(self, s: str) -> bool:
        h=""
        for i in s:
            if i.isalnum():
                h+=i
            else:
                h+=' '
        g=''
        for i in h:
            if i!=' ':
                g+=i
        t=g.lower()
        if t[0:]==t[::-1] or g==' ':
            return True
        else:
            return False
class Solution:
    def isPalindrome(self, s: str) -> bool:
        h=''
        for i in s:
            if i.isalnum():
                h+=i
            else:
                h+=''
        h=h.lower()
        if h==h[::-1]:
            return True
        else:
            return False
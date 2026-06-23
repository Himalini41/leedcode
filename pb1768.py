class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m=min(len(word1),len(word2))
        v=''
        for i in range(m):
            v+=word1[i]
            v+=word2[i]
        v+=word1[m:]
        v+=word2[m:]
        return v
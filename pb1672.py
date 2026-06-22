class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        v=[]
        for i in range(len(accounts)):
            v.append((sum(accounts[i])))
        return max(v)
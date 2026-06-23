class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        m=0
        mi=prices[0]
        for i in prices:
            if i < mi:
                mi=i
            pr=i-mi
            if pr>m:
                m=pr
        return m
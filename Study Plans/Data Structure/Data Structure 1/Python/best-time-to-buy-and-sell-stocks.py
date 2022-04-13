class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        mx = 0
        mi = prices[0]
        
        for price in prices:
            mi = min(mi, price)
            mx = max(mx, price-mi)
        
        return mx
    

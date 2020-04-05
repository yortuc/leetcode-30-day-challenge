class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        ret = 0
        
        # sum positive increases
        for i in range(len(prices) - 1):
            if prices[i+1] > prices[i]:
                ret += prices[i+1] - prices[i]
                
        return ret


# -----------------------------
# 201 / 201 test cases passed.
# Status: Accepted
# Runtime: 52 ms
# Memory Usage: 15 MB
# -----------------------------
class Solution(object):
    def maxProfit(self, prices):
        ret = 0

        l, r = 0, 1
        
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                ret = max(profit, ret)
            else:
                l=r
                
            r+=1

        return ret
        
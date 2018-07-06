class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        import math
        m = math.inf
        ret = -math.inf
        for _ in prices:
            m = _ if _ < m else m
            if m is not math.inf:
                ret = _ - m if _ - m > ret else ret
        
        return max(0, ret)
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # hold sell cooldown empty
        if not prices:
            return 0
        f = [[0] * 4 for _ in range(len(prices))]
        f[0][0] = -prices[0]
        f[0][1] = -float('inf')
        f[0][2] = -float('inf')
        for i in range(1, len(prices)):
            f[i][0] = max(f[i - 1][3], f[i - 1][2]) - prices[i]
            f[i][0] = max(f[i][0], f[i - 1][0])
            f[i][1] = f[i - 1][0] + prices[i]
            f[i][2] = f[i - 1][1]
            f[i][3] = max(f[i - 1][2], f[i - 1][3])
        # print(f)
        return max(f[-1])
        
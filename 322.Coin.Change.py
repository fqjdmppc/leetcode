class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        f = [0] + [float('inf')] * amount
        for _ in range(amount + 1):
            if f[_] < float('inf'):
                for i in coins:
                    if _ + i <= amount:
                        f[_ + i] = min(f[_ + i], f[_] + 1)
        return -1 if f[-1] == float('inf') else f[-1]
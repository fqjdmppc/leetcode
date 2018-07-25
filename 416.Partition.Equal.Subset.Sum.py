class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = sum(nums)
        if s % 2: 
            return False
        else:
            x = s // 2
            f = [True] + [False] * x
            c = set([0])
            for n in nums:
                for _ in list(c):
                    if n + _ <= x:
                        f[n + _] = True
                        c.add(n + _)
                        if f[-1]: return True
        
        return f[-1]
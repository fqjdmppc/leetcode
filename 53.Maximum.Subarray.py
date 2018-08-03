class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ret = -float('inf')
        for _ in nums:
            if _ >= s and s < 0:
                s = _
            else:
                s += _
            
            ret = max(ret, s)
        return ret
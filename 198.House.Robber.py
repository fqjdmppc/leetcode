class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: 
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        a0, a1, b0, b1 = 0, nums[0], nums[0], nums[1]
        for _ in range(2, len(nums)):
            c0, c1 = max(b0, b1), max(a0, a1, b0) + nums[_]
            a0, a1, b0, b1 = b0, b1, c0, c1
            
        return max(b0, b1)
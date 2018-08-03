class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        now_max = 0
        for _ in range(len(nums)):
            if _ > now_max:
                return False
            else:
                now_max = max(now_max, _ + nums[_])
        return True
            
            
        
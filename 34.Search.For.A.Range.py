class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1, -1]
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        if nums[l] != target:
            return [-1, -1]
        else:
            ret = l
        
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m
            else:
                l = m + 1
        return [ret, l if nums[l] == target else (l-1)]
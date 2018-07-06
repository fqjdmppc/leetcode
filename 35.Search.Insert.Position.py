class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        else:
            l, r = 0, len(nums) - 1
            while l != r:
                m = (l + r) // 2
                if target <= nums[m]:
                    r = m
                else:
                    l = m + 1
            return l
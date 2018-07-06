class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while 1:
            if (l == r and nums[l] != target) or r < l:
                return -1
            m = (l + r) // 2
            x = nums[m]
            if  x == target:
                break
            elif (nums[l] <= x <= target <= nums[r]) or (nums[r] < nums[l] and x >= nums[r] and target < x and target <= nums[r]) or (nums[r] >= target > x) or (target > x >=nums[l] and nums[l] > nums[r]):
                l = m + 1
            else:
                r = m
        return m
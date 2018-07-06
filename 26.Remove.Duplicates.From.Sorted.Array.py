class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        else:
            i,j = 0, 1
            while j < len(nums):
                if nums[j] != nums[i]:
                    nums[i + 1] = nums[j]
                    i += 1
                j += 1
            return i + 1
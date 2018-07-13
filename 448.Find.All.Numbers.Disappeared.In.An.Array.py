class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            j = nums[i]
            while j != 0:
                i = nums[j - 1]
                nums[j - 1] = 0
                j = i
        return [_ + 1 for _ in range(len(nums)) if nums[_] != 0]
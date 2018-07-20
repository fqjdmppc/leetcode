class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        z = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                z += 1
            else:
                nums[i] = nums[j]
                i += 1
        for j in range(1, z + 1):
            nums[-j] = 0
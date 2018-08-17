class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            pass
        else:
            ln = len(nums)
            i = ln - 1
            while i >= 1:
                if nums[i - 1] >= nums[i]:
                    i -= 1
                else:
                    break

            if i == ln - 1:
                nums[-2], nums[-1] = nums[-1], nums[-2]
            elif i == 0:
                nums.reverse()
            else:
                for j in range((ln - 1 - i) // 2 + 1):
                    nums[j + i], nums[-1 - j] = nums[-1 - j], nums[j + i]
                for j in range(i, ln):
                    if nums[j] > nums[i - 1]:
                        nums[j], nums[i - 1] = nums[i - 1], nums[j]
                        break
            
            
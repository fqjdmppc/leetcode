class Solution:
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        q = -float('inf')
        x, y = -1, len(nums)
        for _ in range(len(nums) - 1):
            if nums[_] > q:
                q = nums[_]
            if q > nums[_ + 1]:
                x = _ + 1
                
        q = float('inf')
        y = len(nums)
        for _ in range(len(nums) - 1, 0, -1):
            if nums[_] < q:
                q = nums[_]
            if q < nums[_ - 1]:
                y = _ - 1
        
        return (x - y + 1) if y <= x else 0
            
        
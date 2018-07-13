class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = [1]
        for _ in nums:
            a.append(a[-1] * _)
        b = [1]
        for _ in reversed(nums):
            b.append(b[-1] * _)
        b.reverse()
        return [_[0] * _[1] for _ in zip(a[:-1], b[1:])]
        
            
class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        def p(g):
            counter = 0
            l = 0
            for _ in range(len(nums)):
                while nums[_] - nums[l] > g:
                    l += 1
                counter += (_ - l)
            return counter >= k
        
        nums = sorted(nums)
        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if p(m):
                r = m
            else:
                l = m + 1
        
        return l
        
            
        
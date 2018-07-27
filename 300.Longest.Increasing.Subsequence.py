class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = [-float('inf')]
        for _ in nums:
            l, r = 0, len(ret) - 1
            while l < r:
                m = (l + r) // 2
                if ret[m] < _:
                    l = m + 1
                else:
                    r = m
            l += 0 if ret[l] < _ else -1
            if l == (len(ret) - 1):
                ret.append(_)
            else:
                ret[l + 1] = _
            # print(l, ret)
        return len(ret) - 1
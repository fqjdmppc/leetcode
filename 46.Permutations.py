class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def gen(cur, used, not_used, result):
            if len(not_used) == 0:
                result.append(cur.copy())
            else:
                for _ in not_used:
                    gen(cur + [nums[_]], used | set([_]), not_used - set([_]), result)
                    
        ret = []
        gen([], set(), set([_ for _ in range(len(nums))]), ret)
        return ret
                
        
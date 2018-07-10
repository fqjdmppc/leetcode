class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        max_i = len(nums)
        d = [[[_] for _ in range(max_i)]]
        for i in range(1, max_i):
            ret = []
            for j in d[-1]:
                for k in range(j[-1] + 1, max_i):
                    ret.append(j + [k])
            d.append(ret)
        return [[]] + [[nums[d[i][j][k]] for k in range(len(d[i][j]))] for i in range(len(d)) for j in range(len(d[i]))]
            
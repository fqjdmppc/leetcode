class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        idx = dict()
        for i, _ in enumerate(nums):
            if _ not in d:
                d[_] = 1
                idx[_] = [i]
            else:
                d[_] += 1
                idx[_].append(i)
        for _ in d:
            d[_] -= 1
            if (target - _) in d and d[target - _] > 0:
                return [idx[_].pop(), idx[target - _].pop()]
            d[_] += 1
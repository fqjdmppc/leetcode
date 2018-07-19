class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        ftol = dict()
        ltof = dict()
        used = set()
        for _ in nums:
            if _ not in used:
                used.add(_)
                if _ - 1 in ltof:
                    ltof[_] = ltof.pop(_ - 1)
                    ftol[ltof[_]] = _
                    t = _
                    while t + 1 in ftol:
                        x = ftol.pop(t + 1)
                        ltof.pop(x)
                        ftol[ltof[t]] = x
                        ltof[x] = ltof.pop(t)
                        t = x
                elif _ + 1 in ftol:
                    ftol[_] = ftol.pop(_ + 1)
                    ltof[ftol[_]] = _
                else:
                    ftol[_] = _
                    ltof[_] = _
        ret = -float('inf')
        for _ in ftol:
            ret = max(ftol[_] - _, ret)
        # print(ftol)
        return ret + 1
            
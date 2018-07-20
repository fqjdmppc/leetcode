class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        d = {(1 << _) - 1: _ for _ in range(1, 33)}
        ret = [0] * num + [0]
        for _ in range(1, num + 1):
            ret[_] = ret[_ - 1] - d[_ ^ (_ - 1)] + 2
        
        return ret
        
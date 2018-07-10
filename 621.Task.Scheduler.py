class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        from collections import Counter
        c = Counter(tasks)
        total = len(tasks)
        last = dict(zip(c.keys(), [-999] * len(c.keys())))
        ret = 0
        while total:
            q = -0x12345678
            for _ in c:
                if c[_] > 0 and ret - last[_] > n:
                    if c[_] > q:
                        q = c[_]
                        w = _
            if q > -0x12345678:
                total -= 1
                c[w] -= 1
                last[w] = ret
            ret += 1
        return ret
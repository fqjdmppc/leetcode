class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def go(f, left, cur_numbers, ret, dup):
            if left == 0:
                t = str(sorted(cur_numbers))
                if t not in dup:
                    ret.append(cur_numbers)
                    dup.add(t)
            elif left < 0:
                pass
            else:
                for _ in f[left]:
                    go(f, left - _, cur_numbers + [_], ret, dup)
            return
                    
                
        import heapq
        r = [0]
        heapq.heapify(r)
        f = [[] for _ in range(target + 1)]
        for i in candidates:
            t = r.copy()
            while t:
                x = heapq.heappop(t)
                k = 1
                while x + k * i <= target:
                    if not f[x + k * i]:
                        heapq.heappush(r, x + k * i)
                        f[x + k * i].append(i)
                    elif f[x + k * i][-1] != i:
                        f[x + k * i].append(i)
                    k += 1
        ret = []
        go(f, target, [], ret, set())
        return ret
                
            
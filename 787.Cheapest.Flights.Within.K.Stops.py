class Solution:
    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        f = [float("inf")] * n
        f[src] = 0
        for _ in range(0, K + 1):
            nf = f.copy()
            for q,w,e in flights:
                nf[w] = min(f[q] + e, nf[w])
            f = nf
            
        return -1 if f[dst] == float("inf") else f[dst]
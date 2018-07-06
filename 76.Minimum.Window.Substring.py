class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import deque
        def check(d):
            for _ in d:
                if d[_] > 0: return False
            return True
        
        d = dict()
        total = len(t)
        for x in t:
            if x not in d: d[x] = 1
            else: d[x] += 1
        q = deque()
        ret = None
        
        for x in range(len(s)):
            if s[x] in d:
                d[s[x]] -= 1
                q.append(x)
                if check(d):
                    if not ret or x - q[0] < ret[1] - ret[0]:
                        ret = (q[0], x)
                    while d[s[q[0]]] < 0:
                        d[s[q[0]]] += 1
                        q.popleft()
                        if x - q[0] <  ret[1] - ret[0]:
                            ret = (q[0], x)
                    d[s[q[0]]] += 1
                    q.popleft()
                    
        return "" if not ret else s[ret[0]: ret[1] + 1]
                
            
        
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
#         def go(l, r):
#             if l > r: return 0
#             elif l == r: return heights[l]
#             i = j = float('inf')
#             for _ in range(l, r + 1):
#                 if heights[_] < i:
#                     i = heights[_]
#                     j = _
#             return max((r - l + 1) * i, go(l, j - 1), go(j + 1, r))   
#         return go(0, len(heights) - 1)

        # import heapq
        # if not heights: return 0
        # q = [(heights[_], _) for _ in range(len(heights))]
        # heapq.heapify(q)
        # w = [(0, len(heights) - 1)]
        # ret = 0
        # while w:
        #     x = heapq.heappop(q)
        #     for _ in range(len(w)):
        #         if w[_][0] <= x[1] <= w[_][1]:
        #             ret = max(ret, x[0] * (w[_][1] - w[_][0] + 1))
        #             y = w[_]
        #             w = w[ : _] + w[_ + 1:]
        #             if x[1] > y[0]:
        #                 w.append((y[0], x[1] - 1))
        #             if x[1] < y[1]:
        #                 w.append((x[1] + 1, y[1]))
        #             break
        # return ret
        
        if not heights: return 0
        heights.append(-1)
        q = []
        ret = 0
        for _ in range(len(heights)):
            if not q or heights[q[-1]] <= heights[_]:
                q.append(_)
            else:
                i = len(q) - 1
                while i >= 0 and heights[q[i]] > heights[_]:
                    ret = max(ret, (q[-1] - q[i] + 1) * heights[q[i]])
                    i -= 1
                q = q[: i + 1]
                q.append(_)
            print(q, ret)
        return ret
        
    
                
            
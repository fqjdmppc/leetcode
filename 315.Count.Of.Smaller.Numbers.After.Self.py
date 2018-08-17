class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        from collections import deque
        if not nums:
            return []
        else:
            nums.reverse()
            q = deque([nums[0]])
            ret = [0] * len(nums)
            for i in range(1, len(nums)):
                l, r = 0, len(q) - 1
                while l < r:
                    m = (l + r) // 2
                    if nums[i] > q[m]:
                        l = m + 1
                    else:
                        r = m
                l += 0 if nums[i] <= q[l] else 1
                # print(nums[i], l, ' before', q)
                q.rotate(-l)
                q.appendleft(nums[i])
                q.rotate(l)
                # print(nums[i], l, ' after', q)
                ret[i] = l
                # print(nums[i],l, q)
            return list(reversed(ret))
                    
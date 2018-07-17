import random
class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def find(l, r, k):
            if l == r: 
                return nums[l]
            t = nums[random.randint(l, r)]
            q, w = l ,r 
            while q < w:
                if nums[q] > t or (nums[q] == t and random.randint(0, 1)):
                    nums[q], nums[w] = nums[w], nums[q]
                    w -= 1
                else:
                    q += 1
            n = q - l + (0 if nums[q] > t else 1)
            if k > n:
                return find(l + n, r, k - n)
            else:
                return find(l, l + n - 1, k)
            
        return find(0, len(nums) - 1, len(nums) - k + 1)
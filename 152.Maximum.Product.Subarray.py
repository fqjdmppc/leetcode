class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return nums[0]
        else:
            a, b = None, None
            ret = float('-inf')
            for _ in nums:
                if _ >= 0:
                    a, b = max(a * _, _) if a is not None else _, b * _ if b is not None else None
                    ret = max(ret, a if a is not None else float('-inf'), b if b is not None else float('-inf'))
                else:
                    a, b = b * _ if b is not None else None, min(_ * a, _) if a is not None else _ 
                    ret = max(ret, a if a is not None else float('-inf'), b if b is not None else float('-inf'))
                #print(_, ret, a, b)
        return ret
                
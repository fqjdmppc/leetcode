class Solution:
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        hashtable = dict()
        def tohash(depth, target):
            return str(depth) + "&" + str(target)
        
        def go(depth, target):
            if depth == 0:
                return (target == nums[0]) + (target == -nums[0])
            s = tohash(depth, target)
            if s in hashtable: 
                return hashtable[s]
            else:
                hashtable[s] = go(depth - 1, target + nums[depth]) + go(depth - 1, target - nums[depth])
                return hashtable[s]
            
        return go(len(nums) - 1, S)
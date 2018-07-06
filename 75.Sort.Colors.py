class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def p1(x):
            while x[0] < x[1]:
                if nums[x[0]] == 0: 
                    x[0] += 1
                elif nums[x[1]] == 2: 
                    x[1] -= 1
                elif nums[x[0]] == 2 or nums[x[1]] == 0: 
                    nums[x[0]], nums[x[1]] = nums[x[1]], nums[x[0]]
                else:
                    return
        
        def p2(x): #1????1
            i = x[0] + 1
            while x[0] < x[1] and i < x[1]:
                if nums[i] == 1:
                    i += 1
                elif nums[i] == 0:
                    nums[x[0]], nums[i] = nums[i], nums[x[0]]
                    x[0] += 1
                    i += 1
                elif nums[i] == 2:
                    nums[x[1]], nums[i] = nums[i], nums[x[1]]
                    x[1] -= 1
                    i += 1
                    p1(x)
        
        a = [0, len(nums) - 1]
        p1(a)
        p2(a)
                
        
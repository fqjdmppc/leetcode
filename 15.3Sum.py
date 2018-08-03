#         if len(nums) < 3:
#             return []
#         from collections import Counter
#         a = Counter(nums)
#         l = sorted(a.keys())
#         ret = []
#         for i in range(len(l)):
#             for j in range(i, len(l)):
#                 if -l[i] >= 2 *l[j]:
#                     if l[i] == l[j] == 0:
#                         flag = (a[0] >= 3)
#                     elif l[i] == l[j]:
#                         flag = (a[l[i]] >= 2 and a[- l[i] - l[j]])
#                     elif 2 * l[j] == -l[i]:
#                         flag = (a[l[j]] >= 2 and a[l[i]])
#                     else:
#                         flag = (a[l[i]] and a[l[j]] and a[-l[i] - l[j]])
#                     if flag:
#                         ret.append([l[i], l[j], -l[i] - l[j]])
        
#         return ret
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        from collections import Counter
        ret = []
        nums = Counter(nums)
        if nums[0] >= 3:
            ret.append([0,0,0])
        for _ in nums.keys():
            nums[_] = min(2, nums[_])
        nums = sorted(nums.elements())
        print(nums)
        for i in range(len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                l, r = i + 1, len(nums) - 1
                while l < r:
                    x = nums[i] + nums[l] + nums[r]
                    if x == 0:
                        if not ret or nums[i] != ret[-1][0] or nums[l] != ret[-1][1]:
                            ret.append([nums[i], nums[l], nums[r]])
                        l += 1
                        r -= 1
                    elif x < 0:
                        l += 1
                    else:
                        r -= 1
        return ret
    
        
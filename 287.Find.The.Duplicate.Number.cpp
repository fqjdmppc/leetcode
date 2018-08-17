// class Solution:
//     def findDuplicate(self, nums):
//         """
//         :type nums: List[int]
//         :rtype: int
//         """
//         for i, x in enumerate(nums):
//             j = x - 1
//             y = nums[j]
//             l = 2
//             while y != x:
//                 if l > len(nums):
//                     break
//                 else:
//                     l += 1
//                 j = y - 1
//                 y = nums[j]
                
//             if j != i and l <= len(nums):
//                 return x
class Solution {
public:
    int findDuplicate(vector<int>& nums) 
    {
        for(int i = 0;i < nums.size();i++)
        {
            int x = nums[i], j = x - 1,y = nums[j],l = 2;
            while (y != x)
            {
                if (l > nums.size())
                    break;
                else
                    l += 1;
                j = y - 1;
                y = nums[j];
            }
            if (j != i && l <= nums.size())
                return x;
        }
    }
};
// class Solution(object):
//     def subarraySum(self, nums, k):
//         """
//         :type nums: List[int]
//         :type k: int
//         :rtype: int
//         """
//         for i in range(1, len(nums)):
//             nums[i] += nums[i - 1]
//         ret = 0
//         for i in range(len(nums)):
//             for j in range(i, len(nums)):
//                 ret += (nums[j] - (nums[i - 1] if i > 0 else 0) == k)
//         return ret
                
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if (nums.size() > 1)
        {
            for (int i = 1;i < nums.size();i++)
                nums[i] += nums[i - 1];
        }
        int ret = 0;
        for (int i = 0;i < nums.size();i++)
            for (int j = i;j < nums.size(); j++)
                ret += (nums[j] - (i > 0? nums[i - 1]: 0) == k);
        return ret;
    }
};
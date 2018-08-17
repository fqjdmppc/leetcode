class Solution {
public:
    int maxCoins(vector<int>& nums) 
    {
        nums.push_back(1);
        for (int i = nums.size() - 1;i > 0; i--)
            nums[i] = nums[i - 1];
        nums[0] = 1;
        nums.push_back(1);
        unsigned int f[666][666];
        unsigned int ln = nums.size();
        memset(f, 0, sizeof(f));
        for (int k = 2; k < ln; k++)
            for (int i = 0; i < ln - k;i++)
            {
                unsigned int t = nums[i] * nums[i + k];
                for (int j = i + 1;j < i + k; j++)
                    f[i][i + k] = max(f[i][i + k], f[i][j] + f[j][i + k] + t * nums[j]);
            }
        return f[0][ln - 1];
    }
};
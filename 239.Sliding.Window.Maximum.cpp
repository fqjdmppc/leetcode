class Solution {
public:
    void heapadd(vector<int> &q, int val)
    {
        q.push_back(val);
        int i = q.size() - 1;
        int j = (i - 1) >> 1;
        while (i && q[j] < q[i])
        {
            q[j] ^= q[i];
            q[i] ^= q[j];
            q[j] ^= q[i];
            i = j;
            j = (i - 1) >> 1;
        }
    }
    void heapremove(vector<int> &q)
    {
        q[0] = q.back();
        q.pop_back();
        int i = 0;
        int j, x, t;
        while(1)
        {
            j = -1;
            t = q[i];
            x = 2 * i + 1;
            if (x < q.size() && q[x] > t)
            {
                j = x;
                t = q[x];
            }
            if (x + 1 < q.size() && q[x + 1] > t)
            {
                j = x + 1;
            }
            if (j < 0) 
                return;
            else
            {
                q[i] ^= q[j];
                q[j] ^= q[i];
                q[i] ^= q[j];
                i = j;
            }
        }
    }
    // int heappop(vector<int> &q)
    // {
    //     int ret = q[0];
    //     heapremove(q);
    //     return ret;
    // }
    vector<int> maxSlidingWindow(vector<int>& nums, int k) 
    {
        vector<int> qmax, qremoved, ret;
        if (nums.empty()) return nums;
        for(int i = 0;i < k;i++)
            heapadd(qmax, nums[i]);
        ret.push_back(qmax[0]);
        for (int j = k;j < nums.size();j++)
        {
            heapadd(qremoved, nums[j - k]);
            heapadd(qmax, nums[j]);
            while (!qremoved.empty() && qremoved[0] >= qmax[0])
            {
                heapremove(qremoved);
                heapremove(qmax);
            }
            ret.push_back(qmax[0]);
        }
        return ret;
    }
};
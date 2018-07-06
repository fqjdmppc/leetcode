#include <cmath>
class Solution {
public:
    int numSquares(int n) {
        //         max_int = int(n**0.5 + 0.0000001)
        // f = [0, 1, 2, 3, 1] + [None] * n
        // if n <= 4: return f[n]
        // else:
        //     for _ in range(5, n + 1):
        //         if _ % 4 == 0:
        //             f[_] = f[_ // 4]
        //         elif _ % 8 == 7:
        //             f[_] = 4
        //         else:
        //             f[_] = (f[_ - 1] + 1)
        //             for i in range(2, int(_**0.5 + 0.00000001) + 1):
        //                 f[_] = min(f[_], f[_ - i * i] + 1)
        // return f[n]
        unsigned int f[666666] = {0,1,2,3,1};
        if (n <= 4)
            return f[n];
        else
        {
            for (int i = 5 ;i <= n; i++)
            {
                if (i % 4 == 0) f[i] = f[i / 4];
                else if (i % 8 == 7) f[i] = 4;
                else
                {
                    f[i] = f[i - 1] + 1;
                    for (int j = 2; j <= int(sqrt(i) + 0.0000001);j++)
                    {
                        f[i] = min(f[i], f[i - j * j] + 1);
                    }
                }
            }
        }
        return f[n];
        
        
    }
};
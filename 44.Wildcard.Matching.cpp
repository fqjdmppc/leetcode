#include <cstdio>
class Solution {
public:
//     class Solution:
//     def isMatch(self, s, p):
//         """
//         :type s: str
//         :type p: str
//         :rtype: bool
//         """
//         max_len = 2048
//         while "**" in p:
//             p = p.replace("**", "*")
//         if p == '*' or p == s: return True
//         elif p == '' or s == '': return False
//         f = [[False] * max_len for _ in 'a'*max_len]
        
//         if p[0] == "*":
//             f[0] = [True] * max_len
//         elif p[0] == "?" or p[0] == s[0]:
//             f[0] = [True] + [False] * max_len
//         else:
//             return False
//         #print(0, f[0])
//         for i in range(1, len(p)):
//             for j in range(len(s)):
//                 if p[i] == '*':
//                     f[i][j] = (f[i - 1][j] or (f[i][j - 1] if j > 0 else False))
//                 else:
//                     if j == 0:
//                         f[i][j] = (i == 1 and p[0] == "*" and (p[1] == '?' or p[1] == s[0]))
//                     else:
//                         f[i][j] = f[i - 1][j - 1] if (p[i] == '?' or p[i] == s[j]) else False
//             #print(i, f[i])
//         return f[len(p) - 1][len(s) - 1]
                        
    bool isMatch(string s, string p) {
        int max_len = 2048;
        int temp;
        while ((temp = p.find("**")) >= 0)
        {
            p = p.erase(temp, 1);
        }
        if (p == "*" || p == s) return 1;
        else if (p == "" || s == "") return 0;
        int f[2][max_len];
        
        if (p[0] == '*') 
        {
            for (int i = 0;i < max_len;i++)
                f[0][i] = 1;
        }
        else if (p[0] == '?' || p[0] == s[0])
        {
            f[0][0] = 1;
            for (int i = 1;i < max_len;i++)
                f[0][i] = 0;
        }
        else return 0;
        
        for (int i = 1; i < p.length();i++)
        {
            for (int j = 0;j < s.length();j++)
            {
                if (p[i] == '*')
                    f[1][j] = (f[0][j] || (j > 0 ? f[1][j - 1] : 0));
                else if (j == 0)
                    f[1][j] = (i == 1 && p[0] == '*' && (p[1] == '?' || p[1] == s[0]));
                else
                    f[1][j] = (p[i] == '?' || p[i] == s[j]) ? f[0][j - 1] : 0;
            }
            memcpy(f[0], f[1], sizeof(f[1]));
        }
        
        // cout << p.length() << s.length();
        return f[p.length() <= 1? 0 : 1][s.length() - 1];
        // return 1;
    }
};
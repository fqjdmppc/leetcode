class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        m = [[2 if _ != len(s) - 1 and s[_] == s[_ + 1] else 0 for _ in range(len(s))], [1] * len(s)]
        for _ in range(3, len(s) + 1):
            for i in range((_ - 1) // 2, len(s) - _ // 2):
               #print(_, i, m, m[_ % 2][i], (_ - 2), i - _ // 2, i + _ // 2)
                if m[_ % 2][i] == (_ - 2):
                    l = 0 if _ % 2 else 1
                    if s[i - _ // 2 + l] == s[i + _ // 2]:
                        m[_ % 2][i] = _
        
        ri = rm =-0xffff
        print(m)
        for _ in range(len(s)):
            if m[0][_] > rm:
                ri, rm = _ , m[0][_]
            if m[1][_] > rm:
                ri, rm = _ , m[1][_]
        
        return s[ri - rm // 2 + (0 if rm % 2 else 1): ri + rm // 2 + 1]
            
                            
                    
                
        
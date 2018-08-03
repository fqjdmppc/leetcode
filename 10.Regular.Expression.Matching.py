class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        s = '@' + s
        p = '@' + p
        while '**' in p: #fix 'abc***' to 'abc*'
            p = p.replace('**', '*')
        
        s = s + '@'
        p = p + '@'
        
        star_i = set()
        if '*' in p:
            flag = (p[-1] == '*')
            p = p.split("*")
            i = 0
            for _ in p:
                i += len(_)
                star_i.add(i - 1)
            if not flag:
                star_i.remove(max(star_i))
            p = ''.join(p)
        
        
        
        
        print(s, p, star_i)
        f = [False] * len(p)
        f[0] = True
        for i in range(1, len(p)):
            f[i] = (f[i - 1] and i in star_i)
        last = f.copy()
        print(f)
        for i in range(1, len(s)):
            for j in range(len(p)):
                if s[i] == p[j] or p[j] == '.':
                    f[j] = last[j - 1] or (j in star_i and (last[j] or f[j - 1]))
                else:
                    f[j] = (f[j - 1] if j in star_i else False)
            last = f.copy()
            print(f)
            
            
            
        # print('star i', star_i, s, p)
        # i, j = 1, 1
        # while i < len(s) and j < len(p):
        #     if s[i] == p[j] or p[j] == '.':
        #         print(i, j, 1)
        #         i += 1
        #         j += 1
        #     elif j - 1 in star_i:
        #         print(i, j, 2)
        #         if (p[j - 1] == '.' or p[j - 1] == s[i]):
        #             i += 1
        #         else:
        #             j += 1
        #     elif j in star_i:
        #         print(i, j, 3)
        #         star_i.remove(j)
        #         j += 1
        #     else:
        #         print(i, j, 4)
        #         return False
        
        return f[-1]
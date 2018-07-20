class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()
        ret = []
        for _ in strs:
            s = ''.join(sorted(_))
            if s in d:
                ret[d[s]].append(_)
            else:
                ret.append([_])
                d[s] = len(ret) - 1
                
        return ret
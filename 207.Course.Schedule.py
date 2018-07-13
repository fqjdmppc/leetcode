class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        d = {_:set() for _ in range(numCourses)}
        for _ in prerequisites:
            if _[0] not in d:
                d[_[0]] = set([_[1]])
            else:
                d[_[0]].add(_[1])
         
        checked = set()       
        for _ in d:
            if _ not in checked:
                d[_] -= checked
                used = set([_])
                while d[_]:
                    x = d[_].pop()
                    if x in used: return False
                    for i in d[x]:
                        if i not in checked:
                            d[_].add(i)
                    used.add(x)
                checked |= used
            if len(checked) == numCourses: return True
        return True
                
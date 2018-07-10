class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people = sorted(people, key=lambda _:_[0])
        ret = []
        while people:
            i = 0
            flag = False
            ti = 0
            while i < len(people):
                j = i
                while j < len(people) and people[j][0] == people[i][0]:
                    j += 1
                for k in range(i, j):
                    if people[k][1] == len(people) - i - 1:
                        flag = True
                        ti = k
                        break
                if flag:
                    break
                else:
                    i = j
            ret.append(people[ti])
            people = people[:ti] + people[ti + 1:]
        ret.reverse()
        return ret
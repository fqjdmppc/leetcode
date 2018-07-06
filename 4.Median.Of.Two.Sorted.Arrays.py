class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) < 3 or len(nums2) < 3:
            nums1.extend(nums2)
            nums1 = sorted(nums1)
            h = len(nums1) // 2
            return (nums1[h] + nums1[~h]) / 2
        CONST = 0xffffffffffffffffffffffff
        l1, l2 = len(nums1), len(nums2)
        nums1.append(CONST)
        nums2.append(CONST)
        t = l1 + l2
        x = t // 2
        l,r = max(0, x - l2), min(l1, x)
        while 1:
            m = (l + r) // 2
            j = x - m
            if m == 0:
                l_max = nums2[j - 1]
            elif j == 0:
                l_max = nums1[m - 1]
            else:
                l_max = max(nums1[m - 1], nums2[j - 1])
            print(l, r, m)
            r_min = min(nums1[m], nums2[j])
            if l_max <= r_min:
                if (t % 2):
                    return r_min
                else:
                    return (r_min + l_max) / 2
            else:
                if m == 0 or nums2[j - 1] > nums1[m - 1]:
                    l = m + 1
                else:
                    r = m - 1
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # s = []
        # for i in nums1:
        #     if i in nums2:
        #         s.append(i)

        # return s
        c = {}
        s = []
        for i in nums1:
            if i not in c.keys():
                c[i] = 1
            else:
                c[i] +=1

        for i in nums2:
            if i in c and c[i]>0:
                s.append(i)
                c[i] -= 1

        return s
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # import itertools
        num=list()
        # for i,j in zip(range(len(nums1)),range(len(nums2))):
        #     if nums1[i]==nums2[j]:
        #         num.append(nums1[i])
        #         i=i+1
        #         j=j+1
        #         print(num)
        #     if nums1[i]<nums2[j]:
        #         num.append(nums1[i])
        #         j=j
        #         i=i+1
        #     if nums1[i]>nums2[j]:
        #         num.append(nums2[j])
        #         i=i
        #         j=j+1
        # print(num)
        output=0
        for i in nums1:
            num.append(i)
        for j in nums2:
            num.append(j)
                
        num=sorted(num)
        div=len(num)
        med=div/2
        if div%2==0:
            output=float(num[med]+num[med-1])/2
        else:
            output = float(num[med])
        return output




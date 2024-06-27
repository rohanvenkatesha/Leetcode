class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        maj=n/2
        dic=dict()
        if n==1:
            return nums[0]
        for i in nums:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]=dic[i]+1
                if dic[i]>maj:
                    return i
                

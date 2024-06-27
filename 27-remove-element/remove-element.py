class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        x=0
        for i in nums:
            if i != val:
                nums[x]=i
                x=x+1
        return x
        
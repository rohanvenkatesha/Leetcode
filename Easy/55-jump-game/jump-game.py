class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # if len(nums)== 0:
        #     return False

        # if len(nums) == 1 and (nums[0] == 1 or nums[0] == 0):
        #     return True

        # i=1
        # last=len(nums)-1
        # oldi=0
        # while (i<len(nums)):
        #     if last - i == nums[i]:
        #         return True
        #     else:
        #         if oldi == i:
        #             break
        #         else:
        #             oldi=i
        #             i = i + nums[i]
        
        # return False

        gas = 0
        for n in nums:
            if gas < 0:
                return False
            elif n > gas:
                gas = n
            gas= gas -1
            
        return True
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

                # left = 0
        # right = len(nums)-1
        # while left < right:
        #     if nums[left] + nums[right] == target:
        #         return [left, right]
        #     elif nums[left] + nums[right] < target:
        #         left = left + 1
        #     else:
        #         right =  right - 1

        temp=dict()
        for i , n in enumerate(nums):
            print(i,n)
            diff = target - n
            if diff in temp:
                return [temp[diff], i]
            temp[n]=i
            
        
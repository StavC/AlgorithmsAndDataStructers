class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.


        :param nums:
        :return:
        '''
        curr_sum = 0
        max_sum = -9999999999999
        for i in range(len(nums)):

            if curr_sum + nums[i] > nums[i]:
                curr_sum = curr_sum + nums[i]
                max_sum = max(curr_sum, max_sum)
            else:
                curr_sum = nums[i]
                max_sum = max(curr_sum, max_sum)
            '''
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)'''
        return max_sum

class Solution:
    '''
    Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


    '''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        mydict = {}

        for i, num in enumerate(nums):
            if num in mydict and abs(i - mydict[num]) <= k:
                return True
            mydict[num] = i
        return False



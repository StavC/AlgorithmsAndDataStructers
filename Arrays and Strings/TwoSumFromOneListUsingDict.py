class Solution:
    '''Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        mydict = {'': ''}
        i = 0
        for num in nums:
            needToFind = target - num
            if needToFind in mydict:
                return [i, mydict[needToFind]]
            else:
                mydict[num] = i
            i = i + 1




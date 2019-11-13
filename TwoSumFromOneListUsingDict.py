class Solution:
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




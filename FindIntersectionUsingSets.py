class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myset = {''}
        myset2 = {''}
        listToReturn = []
        for num in nums1:
            if num not in myset:
                myset.add(num)
        for num in nums2:
            if num in myset:
                myset2.add(num)
        listt = list(myset2)
        listt.remove('')
        return listt


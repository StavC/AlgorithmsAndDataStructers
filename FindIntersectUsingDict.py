class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mydict = {}
        listToReturn = []
        for num in nums1:
            if num not in mydict:
                mydict[num] = 1
            else:
                mydict[num] = mydict[num] + 1

        for num in nums2:
            if num in mydict and mydict[num] > 0:
                listToReturn.append(num)
                mydict[num] = mydict[num] - 1

        return listToReturn
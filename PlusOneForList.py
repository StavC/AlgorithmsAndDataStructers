class Solution:
    '''Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

'''
    def plusOne(self, digits: List[int]) -> List[int]:

        num = 0
        for i in range(len(digits)):
            num = num * 10 + digits[i]
        num += 1
        num = str(num)
        mylist = []
        for i in (num):
            mylist.append(i)

        return mylist



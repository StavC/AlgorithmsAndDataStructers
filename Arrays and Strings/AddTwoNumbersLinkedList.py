# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
       '''
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            print(divmod(25,10))
            n.next = ListNode(val)
            n = n.next
        return root.next
       :param l1: 
       :param l2: 
       :return: 
       ''''''
       
       
        sum = 0
        num1 = 0
        current = l1
        digit = 1
        while current != None:
            num1 = num1 + current.val * digit
            print(num1)
            digit *= 10
            current = current.next

        current = l2
        digit = 1
        num2 = 0
        while current != None:
            num2 = num2 + current.val * digit
            print(num2)
            digit *= 10
            current = current.next
        sum = num1 + num2

        print(sum)

        sstr = str(sum)
        sstr = sstr[::-1]
        print(sstr)

        head = ListNode(0)
        makehead = True
        for digit in sstr:
            if makehead:
                head.val = digit
                head.next = None
                current = head
                makehead = False
            else:
                temp = ListNode(digit)
                current.next = temp
                current = temp
        return (head)






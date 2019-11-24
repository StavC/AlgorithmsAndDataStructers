# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        num1 = 0
        current = l1
        while current != None:
            num1 = num1 * 10 + current.val
            print(num1)
            current = current.next

        current = l2
        num2 = 0
        while current != None:
            num2 = num2 * 10 + current.val
            print(num2)
            current = current.next
        sum = num1 + num2

        print(sum)
        if sum == 0:
            return ListNode(0)
        head = None
        while sum:
            nextDigit = sum % 10
            print(nextDigit)
            sum = sum // 10
            temp = ListNode(nextDigit)
            temp.next = head
            head = temp
        return head




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        stack = list()
        cursor = dummy

        while cursor:
            stack.append(cursor)
            cursor = cursor.next

        for i in range(n):
            stack.pop()

        pre = stack[-1]
        pre.next = pre.next.next

        return dummy.next

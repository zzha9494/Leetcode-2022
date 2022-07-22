# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        cur = dummy

        while cur.next and cur.next.next:
            front = cur.next
            back = front.next
            cur.next = back
            front.next = back.next
            back.next = front
            cur = front

        return dummy.next

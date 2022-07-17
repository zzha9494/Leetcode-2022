from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # base case
        if len(lists) == 0:
            return None

        if len(lists) < 2:
            return lists[0]

        # divide
        mid = len(lists) // 2
        left = lists[:mid]
        right = lists[mid:]

        # recur
        sorted_left = self.mergeKLists(left)
        sorted_right = self.mergeKLists(right)

        # conquer
        return self.merge(sorted_left, sorted_right)

    @staticmethod
    def merge(left: ListNode, right: ListNode):
        dummy = ListNode()
        cur = dummy
        cur1 = left
        cur2 = right
        while cur1 or cur2:
            if not cur1:
                cur.next = cur2
                return dummy.next
            elif not cur2:
                cur.next = cur1
                return dummy.next
            elif cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
                cur = cur.next
            else:
                cur.next = cur2
                cur2 = cur2.next
                cur = cur.next
        return dummy.next

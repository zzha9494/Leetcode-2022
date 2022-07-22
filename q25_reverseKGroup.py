# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        cur = head

        for i in range(k):
            if cur:
                stack.append(cur)
                cur = cur.next
            else:
                break

        if len(stack) != k:
            return head
        else:
            newhead = self.reverseKGroup(cur, k)
            cur = newhead
            while stack:
                temp = stack.pop(0)
                temp.next = cur
                cur = temp

        return cur

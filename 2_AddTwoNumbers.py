from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nxt_val = 0
        res: Optional[ListNode] = ListNode()
        node: Optional[ListNode] = res
        while l1 or l2 or nxt_val != 0:
            n1 = l1.val if l1 else 0
            n2 = l2.val if l2 else 0

            val = n1 + n2 + nxt_val
            curr_val = val % 10
            nxt_val = val // 10

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            node.val = curr_val
            node.next = ListNode() if l1 or l2 or nxt_val != 0 else None
            node = node.next

        return res

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    carry = 0
    out = ListNode()
    ptr = out

    while l1 is not None or l2 is not None or carry != 0:
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0

        x = a + b + carry
        carry = x // 10
        ptr.next = ListNode(x % 10)
        ptr = ptr.next

        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return out.next
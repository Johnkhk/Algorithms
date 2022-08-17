class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


a=b=ListNode() # Referencing the same node, when we do a=a.next, a is just pointing to the next node.
a.val=3
c=ListNode()
c.val=69
a.next=c
a=a.next
print(a.val,b.val)

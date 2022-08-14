def rev(head):
    if not head or not head.next:
        return head
    
    p = rev(head.next)
    head.next.next=head
    head.next = None
    return p
    
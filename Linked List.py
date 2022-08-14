### Reverse Linked-List, (recursive) ###
def rev(head):
    if not head or not head.next:
        return head

    p = rev(head.next)
    head.next.next=head
    head.next = None
    return p
### Reverse Linked-List, (Iterative clean) ###
def reverse(root):
    prev=None
    while root:
        root.next,prev,root=prev,root,root.next
    return prev
### Merge 2 sorted Linked List (iterative) ###
if not list1:
    return list2
if not list2:
    return list1
dummy = ListNode()
tail = dummy
while list1 and list2:
    if list1.val < list2.val:
        tail.next=list1
        list1=list1.next
    else:
        tail.next=list2
        list2=list2.next
    tail=tail.next
if not list1:
    tail.next=list2
elif not list2:
    tail.next=list1
return dummy.next

### Merge 2 sorted Linked List (recursive) ###
def merge(l1,l2):
    if not l1:
        return l2
    if not l2:
        return l1
    if l1.val<l2.val:
        l1.next = merge(l1.next,l2)
        return l1
    else:
        l2.next = merge(l1,l2.next)
        return l2

### Merge 2 Linked List - Alternating (recursive) ###
def merge(l1,l2):
    if not l1 or not l2:
        return None
    l1.next = merge(l2,l1.next)
    return l1
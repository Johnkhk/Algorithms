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
def Merge_2_sorted():
    dummy = tail = ListNode() # Generally a good technique
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


### reverse nodes in k group (detailed explanatoin) ###

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # goal: reverse nodes in k group
        # idea: get prevnode before kgroup and afternode after kgroup, then reverse the kgroup and connect
        dummy=prevNode=ListNode(next=head)
        while True:
            # get kth node
            kthnode= self.getkth(prevNode,k) # [1,2,3] k=2 -> 3
            # if its null, k didn't reach its end, 
            # we break because the question says we can leave the rest as is
            if not kthnode:
                break
                
            # get after node
            afterNode=kthnode.next 
            
            # we want to reverse starting from prevNode.next (start of group)
            # we also want the previous node, which is after we reverse 
            # to not point to NONE but rather to afterNode
            prev,cur = afterNode,prevNode.next
            
            # start the reverse
            # We only want to reverse up till afterNode, not the whole list
            while cur!=afterNode:
                cur.next,prev,cur = prev,cur,cur.next
            
            # After we reverse we need to set the correct value of prevNode for next iteration
            # prevNode should now be prevNode.next because prevNode.next use to be right after prevNode
            # but now it is at the end after reversed, which is what we need prevNode to be after reversing
            # Also, we need to set prevNode.next to point to the group we just reversed's head
            # This will be prev, because after reversing, prev is the head
            prevNode.next,prevNode = prev,prevNode.next
            
        return dummy.next
    
    def getkth(self,root,k):
        for i in range(k):
            if root:
                root=root.next
        return root
            
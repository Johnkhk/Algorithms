
### Divide & Conquer ###
# TC: 
# SC: 
class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
    
    def merge1(self, l, r):
        if not l or not r:
            return l or r
        if l.val< r.val:
            l.next = self.merge(l.next, r)
            return l
        r.next = self.merge(l, r.next)
        return r

### Heap Solution ###
# TC: O(nlog(k)), n is total number of nodes, k is number of lists, better than O(k)
# SC: 
def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    # goal: merge k sorted lists
    # idea: use bfs on heap to get lowest value and build result
    
    h=[]
    for i,l in enumerate(lists):
        if l:
            heapq.heappush(h,(l.val,i))
            lists[i]=lists[i].next
            
    
    # ret = ListNode()
    # dummy = ListNode()
    # ret.next=dummy
    ret=dummy=ListNode()
    
    while h:
        val,idx = heapq.heappop(h)
        # node = lists[idx]
        node = ListNode(val)
        dummy.next=node
        dummy=dummy.next
        lists[idx]
        if lists[idx]:
            heapq.heappush(h,(lists[idx].val,idx))
            lists[idx]=lists[idx].next
    return ret.next
            
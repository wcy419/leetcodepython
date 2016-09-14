# Definition for singly-linked list.
import heapq
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """ :type lists: List[ListNode] :rtype: ListNode """
        heap = []
        for l in lists:
            if l != None:
                heap.append((l.val,l))
        heapq.heapify(heap)
        dummy = ListNode(0)
        cur = dummy
        while heap:
            _,h = heapq.heappop(heap)
            cur.next = h
            cur = cur.next
            if h.next:
                heapq.heappush(heap,(h.next.val,h.next))
        return dummy.next

if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(4)
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list3 = ListNode(3)
    
    print Solution().mergeKLists([list1, list2, list3])


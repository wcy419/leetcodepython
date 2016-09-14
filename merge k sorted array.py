
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):		
        if self:		
            return "{} -> {}".format(self.val, self.next)


# Time:  O(nlogk)
# Space: O(k)
# Heap solution.
import heapq
class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        
        heap = []
        for sorted_list in lists:
            if sorted_list:
                heapq.heappush(heap, (sorted_list.val, sorted_list))
                
        while heap:
            smallest = heapq.heappop(heap)[1]
            current.next = smallest
            current = current.next
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, smallest.next))
                
        return dummy.next
    
class Solution2:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        dummy = ListNode(0)
        current = dummy
        
        ret, heap = [], []
        for lst in lists:
            while lst:
                heapq.heappush(heap, lst.val)
                lst = lst.next

        while heap:
            ret.append(heapq.heappop(heap))
        return ret


if __name__ == "__main__":
    list1 = ListNode(1)
    list1.next = ListNode(3)
    list1.next.next = ListNode(4)
    list2 = ListNode(2)
    list2.next = ListNode(4)
    list3 = ListNode(3)
    
    print Solution().mergeKLists([list1, list2, list3])

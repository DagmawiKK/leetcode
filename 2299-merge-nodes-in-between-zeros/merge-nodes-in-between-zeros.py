# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        sum_nodes = 0
        temp = head.next
        
        while temp:
            if temp.val == 0:
                if sum_nodes != 0:
                    current.next = ListNode(sum_nodes)
                    current = current.next
                    sum_nodes = 0
            else:
                sum_nodes += temp.val
            temp = temp.next

        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = None
        if not list1 and not list2:
            return None
        if not list1:
            return list2
        if not list2:
            return list1
        # while list1 and list2:
        #     if list1.val
